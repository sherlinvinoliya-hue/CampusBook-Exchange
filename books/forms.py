from django import forms
from .models import ContactRequest,Report
class ContactRequestForm(forms.ModelForm):
    class Meta:
        model=ContactRequest; fields=('message','optional_contact'); widgets={'message':forms.Textarea(attrs={'rows':4,'placeholder':'Hi, I am interested in this book. Is it still available?'})}
class ReportForm(forms.ModelForm):
    class Meta:
        model=Report; fields=('reason','details'); widgets={'details':forms.Textarea(attrs={'rows':3})}
