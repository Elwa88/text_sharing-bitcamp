from django import forms
from .models import Text

class Textform(forms.ModelForm):
    class Meta:
        model = Text
        fields = ['title','text']