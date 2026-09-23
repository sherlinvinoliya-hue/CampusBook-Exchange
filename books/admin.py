from django.contrib import admin
from .models import Favorite,ContactRequest,Report
admin.site.register(Favorite)
@admin.register(ContactRequest)
class ContactAdmin(admin.ModelAdmin): list_display=('book','buyer','seller','status','created_at'); list_filter=('status',)
@admin.register(Report)
class ReportAdmin(admin.ModelAdmin): list_display=('book','reporter','reason','resolved','created_at'); list_filter=('reason','resolved'); list_editable=('resolved',)
