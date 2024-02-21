from django.shortcuts import render
from django.contrib import messages
from .models import Contact
from .forms import ContactForm

# Create your views here.
def contact_me(request):
    """
    Renders the most recent information on the website author
    and allows user contact requests.

    Displays an individual instance of :model:`contact.Contact`.

    **Context**
    ``contact``
        The most recent instance of :model:`contact.Contact`.
        ``contact_form``
            An instance of :form:`contact.ContactForm`.
    
    **Template**
    :template:`contact/contact.html`
    """

    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.add_message(request, messages.SUCCESS, "Message sent! I endeavour to respond within 2 working days.")

    """
    Renders the Contact page
    """
    contact = Contact.objects.all().order_by('-updated_on').first()
    contact_form = ContactForm()

    return render(
        request,
        "contact/contact.html",
        {
            "contact": contact,
            "contact_form": contact_form,
            },
    )