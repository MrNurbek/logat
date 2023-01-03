from main.models import *
from django.forms import ModelForm

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"
