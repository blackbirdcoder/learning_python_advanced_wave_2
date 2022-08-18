from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth import logout
from .forms import RegistrationForm, LoginForm, ProfileEditingNameForm, ProfileEditingEmail
from .utils import Manager


def custom_registration(request):
    context = {
        'heading': 'Join us',
        'form': RegistrationForm(),
        'button_name': 'Registration'
    }
    manager = Manager(request, context, RegistrationForm)
    if manager.executor(manager.create):
        return HttpResponseRedirect(reverse_lazy('login'))
    return render(request, 'users/form.html', context)


def custom_login(request):
    context = {
        'heading': 'Login',
        'form': LoginForm(),
        'button_name': 'Login'
    }
    manager = Manager(request, context, LoginForm)
    if manager.executor(manager.user_login):
        return HttpResponseRedirect(reverse_lazy('main'))
    return render(request, 'users/form.html', context)


def profile_editing_names(request):
    context = {
        'heading': 'Change names',
        'form': ProfileEditingNameForm(),
        'button_name': 'Change'
    }
    manager = Manager(request, context, ProfileEditingNameForm)
    if manager.executor(manager.save):
        return HttpResponseRedirect(reverse_lazy('profile'))
    return render(request, 'users/form.html', context)


def profile_editing_email(request):
    context = {
        'heading': 'Change email',
        'form': ProfileEditingEmail(),
        'button_name': 'Change'
    }
    manager = Manager(request, context, ProfileEditingEmail)
    if manager.executor(manager.save):
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
