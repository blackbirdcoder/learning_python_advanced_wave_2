from django.shortcuts import render
from data import context


def product(request, num):
    shop_product = {}
    for value in context['products']:
        if num == value.get('id'):
            shop_product = value
            break
    shop_product['title'] = 'Buy goods'
    print(shop_product)
    return render(request, 'products/products.html', shop_product)
