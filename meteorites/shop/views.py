from django.http import Http404
from django.shortcuts import render
from shop.models import Product


def main(request):
    context = {
        'title': 'Main',
        'products': Product.objects.all()
    }
    if request.method == 'GET':
        country = request.GET.get('country', '0')
        material_id = request.GET.get('material_id', '0')
        if country != '0':
            context['products'] = Product.objects.filter(location=country)
        if material_id != '0':
            context['products'] = Product.objects.filter(category_id=material_id)
        if country != '0' and material_id != '0':
            context['products'] = Product.objects.filter(location=country, category_id=material_id)
    return render(request, 'shop/main.html', context)


def product(request, slug):
    try:
        context = {
            'title': 'Buy Goods',
            'product': Product.objects.get(slug_name=slug)
        }
        return render(request, 'product/product.html', context)
    except Product.DoesNotExist:
        raise Http404('Not found')


def profile(request):
    context = {
        'title': 'Profile',
        'firstname': 'Richard',
        'lastname': 'Stallman',
        'credit': 10000000,
    }
    return render(request, 'user/profile.html', context)
