from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from .models import Advert
#User = get_user_model()

class AdvertForm(forms.ModelForm):
    
    class Meta:
        model = Advert
        fields = ['type', 'title', 'description', 'price', 'number_of_rooms', 'area', 'thumbnail']

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=150, required=True)
    first_name = forms.CharField(max_length=150, required=True)
    last_name = forms.CharField(max_length=150, required=False)
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    confirm_password = forms.CharField(widget=forms.PasswordInput, required=True)
    User = get_user_model()

    def clean(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise ValidationError("Must confirm password")
        return self.cleaned_data

    def clean_username(self):
        username = self.cleaned_data['username']
        r = self.User.objects.filter(username=username)
        if r.count():
            raise ValidationError("username already exists")
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        User = get_user_model()
        r = self.User.objects.filter(email=email)
        if r.count():
            raise ValidationError("email already exists")
        return email
    
    def save(self, commit=True):
        user = self.User.objects.create_user(
            username=self.cleaned_data['username'],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password'],
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name']
        )
        return user
