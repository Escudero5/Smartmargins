from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from account.models import Account

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(
        label = '',
        max_length = 60,
        widget=forms.EmailInput(attrs={'class':'form-control', 'type':'email', 'align':'center', 'placeholder':'Enter Email'}),

    )

    password1 = forms.CharField(
        label = '',
        help_text = 'Make sure to enter a strong password',
        widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password', 'align':'center', 'placeholder':'Enter Password'}),
    )

    password2 = forms.CharField(
        label = '',
        widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password', 'align':'center', 'placeholder':'Re-enter Password'}),
    )

    first_name = forms.CharField(
        max_length = 30,
        label = '',
        widget = forms.TextInput(attrs = {'class':'form-control', 'placeholder': 'First Name'})
    )

    last_name = forms.CharField(
        max_length = 30,
        label = '',
        widget = forms.TextInput(attrs = {'class':'form-control', 'placeholder': 'Last Name'})
    )

    class Meta:
        model = Account
        error_messages = {
        'email': {
            'required': "Email is Required",
           }
           }
        fields = ('email','first_name','last_name','password1','password2')



class AccountAuthenticationForm(forms.ModelForm):
    email = forms.CharField(
    label = '',
    widget = forms.EmailInput(attrs={'class':'form-control', 'type':'email', 'align':'center', 'placeholder':'Email'})
    )

    password = forms.CharField(
    label = '',
    widget = forms.PasswordInput(attrs={'class':'form-control', 'type':'password', 'align':'center', 'placeholder':'Password'}))

    class Meta:
        model = Account
        fields = ('email','password')

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']

            if not authenticate(email = email, password = password):
                raise forms.ValidationError("Invalid Login")
