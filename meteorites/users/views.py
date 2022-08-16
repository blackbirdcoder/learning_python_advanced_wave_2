from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout


def custom_registration(request):
    if request.method == 'POST':
        current_username = request.POST['username']
        if User.objects.filter(username=current_username):
            request.session['notification'] = 'User exists'
            return HttpResponseRedirect(reverse_lazy('registration'))
        password_one = request.POST['password_one']
        password_two = request.POST['password_two']
        if password_one == password_two:
            User.objects.create_user(
                username=current_username,
                email=None,
                password=password_one,
                first_name=request.POST['firstname'],
                last_name=request.POST['lastname']
            )
            return HttpResponseRedirect(reverse_lazy('login'))
    return render(request, 'users/registration.html')


def custom_login(request):
    if request.method == 'POST':
        user = authenticate(
            username=request.POST['username'],
            password=request.POST['password_one']
        )
        if user is None:
            return HttpResponseRedirect(reverse_lazy('login'))
        login(request, user)
        return HttpResponseRedirect(reverse_lazy('main'))
    return render(request, 'users/login.html')


def profile(request):
    context = {
        'title': 'Profile',
        'credit': 10000000,
    }
    if request.user.is_authenticated:
        return render(request, 'users/profile.html', context)
    return HttpResponseRedirect(reverse_lazy('authorization'))


def user_exit(request):
    logout(request)
    return HttpResponseRedirect(reverse_lazy('main'))
