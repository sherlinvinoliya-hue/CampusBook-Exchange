from django.conf import settings
from django.db import models
from books.models import Book

class Favorite(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='favorites'); book=models.ForeignKey(Book,on_delete=models.CASCADE,related_name='favorites'); created_at=models.DateTimeField(auto_now_add=True)
    class Meta: constraints=[models.UniqueConstraint(fields=['user','book'],name='unique_favorite')]

class ContactRequest(models.Model):
    STATUSES=[('new','New'),('read','Read'),('responded','Responded'),('closed','Closed')]
    buyer=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='sent_contact_requests'); seller=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='received_contact_requests')
    book=models.ForeignKey(Book,on_delete=models.CASCADE,related_name='contact_requests'); message=models.TextField(max_length=1200); optional_contact=models.CharField(max_length=120,blank=True)
    status=models.CharField(max_length=20,choices=STATUSES,default='new',db_index=True); created_at=models.DateTimeField(auto_now_add=True)
    class Meta: ordering=['-created_at']

class Report(models.Model):
    REASONS=[('incorrect','Incorrect information'),('fake','Fake listing'),('spam','Spam'),('inappropriate','Inappropriate content'),('sold','Already sold'),('other','Other')]
    reporter=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='reports'); book=models.ForeignKey(Book,on_delete=models.CASCADE,related_name='reports'); reason=models.CharField(max_length=30,choices=REASONS); details=models.TextField(blank=True,max_length=1000); created_at=models.DateTimeField(auto_now_add=True); resolved=models.BooleanField(default=False)
    class Meta: ordering=['-created_at']
