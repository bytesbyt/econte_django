from django.test import TestCase
from .forms import ContactForm


class TestContactForm(TestCase):

    def test_form_is_valid(self):
        """ Test for all fields"""
        form = ContactForm({
            'name': 'tes',
            'email': 'test@test.com',
            'message': 'Hello!'
        })
        self.assertTrue(form.is_valid(), msg="Form is not valid")
