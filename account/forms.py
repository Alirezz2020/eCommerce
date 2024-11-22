from django import forms
from django.core.exceptions import ValidationError
from account.models import MyUser, OtpCode


class UserRegistrationForm(forms.Form):
    email = forms.EmailField()
    full_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))

    def clean_email(self):
        email = self.cleaned_data['email']
        user = MyUser.objects.filter(email=email).exists()
        if user:
            raise forms.ValidationError('Email already registered')
        return email

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        user = MyUser.objects.filter(phone_number=phone_number).exists()
        if user:
            raise forms.ValidationError('Phone number already registered')
        OtpCode.objects.filter(phone_number=phone_number).delete()
        return phone_number

class VerifyCodeForm(forms.Form):
    code = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control'}))



class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())
    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        user = MyUser.objects.get(username=username)
        if not user.check_password(password):
            raise ValidationError('Incorrect username or password')

