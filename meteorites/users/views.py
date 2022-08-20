from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth import logout, login
from .forms import RegistrationForm, LoginForm, ProfileEditingNameForm, ProfileEditingEmail


def custom_registration(request):
    context = {
        'heading': 'Join us',
        'form': RegistrationForm(),
        'button_name': 'Registration'
    }
    if request.method == 'POST':
        context['form'] = RegistrationForm(request.POST)
        if context['form'].is_valid():
            context['form'].create_user()
            return HttpResponseRedirect(reverse_lazy('login'))
    return render(request, 'users/form.html', context)


def custom_login(request):
    context = {
        'heading': 'Login',
        'form': LoginForm(),
        'button_name': 'Login'
    }
    if request.method == 'POST':
        context['form'] = LoginForm(request.POST)
        if context['form'].is_valid():
            login(request, context['form'].user)
            return HttpResponseRedirect(reverse_lazy('main'))
    return render(request, 'users/form.html', context)


def profile_editing_names(request):
    context = {
        'heading': 'Change names',
        'form': ProfileEditingNameForm(),
        'button_name': 'Change'
    }
    if request.method == 'POST':
        context['form'] = ProfileEditingNameForm(request.POST)
        if context['form'].is_valid():
            context['form'].save(request.user)
            return HttpResponseRedirect(reverse_lazy('profile'))
    return render(request, 'users/form.html', context)


def profile_editing_email(request):
    context = {
        'heading': 'Change email',
        'form': ProfileEditingEmail(),
        'button_name': 'Change'
    }
    if request.method == 'POST':
        context['form'] = ProfileEditingEmail(request.POST)
        if context['form'].is_valid():
            context['form'].save(request.user)
            return HttpResponseRedirect(reverse_lazy('profile'))
    return render(request, 'users/form.html', context)


def profile(request):
    context = {
        'title': 'Profile',
        'credit': 10000,
    }
    if request.user.is_authenticated:
        return render(request, 'users/profile.html', context)
    return HttpResponseRedirect(reverse_lazy('authorization'))


def user_exit(request):
    logout(request)
    return HttpResponseRedirect(reverse_lazy('main'))
