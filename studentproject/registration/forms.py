from django import forms
from django.core import validators
#DataFlair #Form
class SignUp(forms.Form):
    first_name = forms.CharField(initial = 'First Name', )
    last_name = forms.CharField()
    email = forms.EmailField(help_text = 'write your email', )
    Address = forms.CharField(required = False, )
    Technology = forms.CharField(initial = 'Django', disabled = True, )
    age = forms.IntegerField()
    password = forms.CharField(widget = forms.PasswordInput, validators=[validators.MinLengthValidator(8)])
    re_password = forms.CharField(help_text = 'renter your password', widget = forms.PasswordInput)
    
    #Validation #DataFlair
    def clean_password(self):
        password=self.cleaned_data['password']
        if len(password)<8:
            raise forms.ValidationError['password is too short. at least 8 letters']
        return password