from django.shortcuts import render
from data import context, userdata


def main(request):
    return render(request, 'shop/main.html', context)


def product(request, num):
    shop_product = {}
    for value in context['products']:
        if num == value.get('id'):
            shop_product = value
            break
    shop_product['title'] = 'Buy goods'
    return render(request, 'product/product.html', shop_product)


def profile(request):
    return render(request, 'user/profile.html', userdata)
