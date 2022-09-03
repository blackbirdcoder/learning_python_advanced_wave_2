from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate, login
from .models import UserModel


class RegistrationForm(forms.Form):
    username = forms.CharField(
        max_length=32,
        label='*Username:',
    )
    first_name = forms.CharField(
        max_length=32,
        label='*First name:'
    )
    last_name = forms.CharField(
        max_length=32,
        label='*Last name:'
    )
    user_email = forms.EmailField(
        label='*Email:'
    )
    password_one = forms.CharField(
        max_length=128,
        label='*Password:',
        widget=forms.PasswordInput
    )
    password_two = forms.CharField(
        max_length=128,
        label='*Password:',
        widget=forms.PasswordInput
    )

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            if UserModel.objects.get(username=username):
                raise ValidationError('User Exists!')
        except UserModel.DoesNotExist as error:
            return username

    def clean(self):
        password_one = self.cleaned_data['password_one']
        password_two = self.cleaned_data['password_two']
        if password_one != password_two:
            raise ValidationError('Passwords not match')

    def create_user(self):
        UserModel.objects.create_user(
            username=self.cleaned_data['username'],
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            email=self.cleaned_data['user_email'],
            password=self.cleaned_data['password_one']
        )


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=32,
        label='Username:',
    )
    password = forms.CharField(
        max_length=128,
        label='Password',
        widget=forms.PasswordInput
    )

    def __init__(self, *args, **kwargs):
        self.user = None
        super().__init__(*args, **kwargs)

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        self.user = authenticate(
            username=username,
            password=password
        )
        if self.user is None:
            raise ValidationError('Wrong data')


class ProfileEditingNameForm(forms.Form):
    first_name = forms.CharField(
        max_length=32,
        label='*First name:'
    )
    last_name = forms.CharField(
        max_length=32,
        label='*Last name:'
    )

    def __init__(self, *args, **kwargs):
        self.user = None
        super().__init__(*args, **kwargs)

    def save(self, user):
        first_name = self.cleaned_data['first_name']
        last_name = self.cleaned_data['last_name']
        UserModel.objects.filter(pk=user.pk).update(
            first_name=first_name,
            last_name=last_name
        )


class ProfileEditingEmail(forms.Form):
    user_email = forms.EmailField(label='*Email:')

    def save(self, user):
        user_email = self.cleaned_data['user_email']
        UserModel.objects.filter(pk=user.pk).update(email=user_email)
