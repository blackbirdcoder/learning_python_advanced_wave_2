from django.shortcuts import render
from django.http import HttpResponse


def profile(request):
    context = {
        'title': 'Profile',
        'firstname': 'Richard',
        'lastname': 'Stallman',
        'credit': 10000000,
    }
    return render(request, 'user/profile.html', context)
