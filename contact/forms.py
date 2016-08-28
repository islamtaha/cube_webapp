from django import forms
from contact.models import ContactMessage


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['full_name', 'email', 'phone_no', 'message']
