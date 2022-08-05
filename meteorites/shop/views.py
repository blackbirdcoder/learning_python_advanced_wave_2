from django.shortcuts import render
from django.http import HttpResponse
from data import context


def index(request):
    return render(request, 'shop/index.html', context)
