from .models import ContactRequest
from django import forms


class ContactForm(forms.ModelForm):
    """
    Form class for users to request a contact
    """
    class Meta:
        """
        Specify the django model and order of the fields
        """
        model = ContactRequest
        fields = ('name', 'email', 'message')

