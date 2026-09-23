from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404,redirect,render
from books.models import Book
from .models import Favorite,ContactRequest
from .forms import ContactRequestForm,ReportForm

@login_required
def toggle_favorite(request,pk):
    book=get_object_or_404(Book,pk=pk,is_approved=True)
    fav,created=Favorite.objects.get_or_create(user=request.user,book=book)
    if not created: fav.delete(); state=False
    else: state=True
    if request.headers.get('x-requested-with')=='XMLHttpRequest':
        from django.http import JsonResponse
        return JsonResponse({'favorited':state})
    messages.success(request,'Saved to favorites.' if state else 'Removed from favorites.'); return redirect(request.META.get('HTTP_REFERER',book.get_absolute_url()))

@login_required
def favorites(request): return render(request,'interactions/favorites.html',{'favorites':Favorite.objects.filter(user=request.user).select_related('book').prefetch_related('book__images')})

@login_required
def contact_seller(request,pk):
    book=get_object_or_404(Book,pk=pk,is_approved=True)
    if book.seller==request.user: messages.info(request,'This is your own listing.'); return redirect(book)
    form=ContactRequestForm(request.POST or None,initial={'message':'Hi, I am interested in this book. Is it still available?'})
    if request.method=='POST' and form.is_valid():
        obj=form.save(commit=False); obj.buyer=request.user; obj.seller=book.seller; obj.book=book; obj.save(); messages.success(request,'Your message was sent to the seller.'); return redirect(book)
    return render(request,'interactions/contact.html',{'form':form,'book':book})

@login_required
def messages_inbox(request):
    incoming=ContactRequest.objects.filter(seller=request.user).select_related('buyer','book'); outgoing=ContactRequest.objects.filter(buyer=request.user).select_related('seller','book')
    return render(request,'interactions/messages.html',{'incoming':incoming,'outgoing':outgoing})

@login_required
def message_status(request,pk,status):
    msg=get_object_or_404(ContactRequest,pk=pk,seller=request.user)
    if request.method=='POST' and status in dict(ContactRequest.STATUSES): msg.status=status; msg.save(update_fields=['status'])
    return redirect('messages_inbox')

@login_required
def report_listing(request,pk):
    book=get_object_or_404(Book,pk=pk,is_approved=True); form=ReportForm(request.POST or None)
    if request.method=='POST' and form.is_valid():
        obj=form.save(commit=False); obj.reporter=request.user; obj.book=book; obj.save(); messages.success(request,'Report submitted for admin review.'); return redirect(book)
    return render(request,'interactions/report.html',{'form':form,'book':book})
