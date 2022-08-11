from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout


def user_authorization(request):
    if request.method == 'POST':
        if request.POST['command'] == 'registration':
            current_username = request.POST['username_reg']
            if User.objects.filter(username=current_username):
                request.session['notification'] = 'User exists'
                request.session['class'] = 'error'
                return HttpResponseRedirect(reverse_lazy('authorization'))
            password_one = request.POST['password_one_reg']
            password_two = request.POST['password_two_reg']
            if password_one == password_two:
                User.objects.create_user(
                    username=current_username,
                    email=None,
                    password=password_one,
                    first_name=request.POST['firstname'],
                    last_name=request.POST['lastname']
                )
                request.session['notification'] = 'Successfully'
                request.session['class'] = 'successfully'
                return HttpResponseRedirect(reverse_lazy('authorization'))
        if request.POST['command'] == 'login':
            user = authenticate(
                username=request.POST['username_log'],
                password=request.POST['password_one_log']
            )
            if user is None:
                request.session['notification'] = 'No user'
                return HttpResponseRedirect(reverse_lazy('authorization'))
            login(request, user)
            return HttpResponseRedirect(reverse_lazy('main'))
    return render(request, 'users/authorization.html')


def profile(request):
    context = {
        'title': 'Profile',
        'firstname': request.user.first_name,
        'lastname': request.user.last_name,
        'credit': 10000000,
        'super': False
    }
    if request.user.is_superuser:
        context['super'] = True
    if request.user.is_authenticated:
        return render(request, 'users/profile.html', context)
    return HttpResponseRedirect(reverse_lazy('authorization'))


def user_exit(request):
    logout(request)
    return HttpResponseRedirect(reverse_lazy('main'))
