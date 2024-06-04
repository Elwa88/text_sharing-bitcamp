from django import forms

class Userform(forms.Form):
    username = forms.CharField(label='username',
                               widget=forms.TextInput({'class':'text-input'}))
    password = forms.CharField(label='password',
                               widget=forms.PasswordInput({'class':'text-input'}))
