from django.shortcuts import render
from django.http import HttpResponse

context = {
        'title': 'Main',
        'products': [
            {
                'id': 1,
                'price': 480000,
                'desc': 'Certified meteorite "Sericho SRH9005", 4.075 kg (Kenya)',
                'dim': '180x135x100 mm',
                'weight': '4075 g',
                'location': 'Kenya',
                'img': 'shr',
            },
            {
                'id': 2,
                'price': 14240,
                'desc': 'Certified meteorite "NWA 7831 HEDB0001" 10.12 g (Western Sahara)',
                'dim': '24,5х20,5x16 mm',
                'weight': '10,12 g',
                'location': 'Western Sahara (Morocco)',
                'img': 'nwa',
            },
            {
                'id': 3,
                'price': 20960,
                'desc': 'Tektite "Philippinite PTB0002", 95.2 g (Philippines)',
                'dim': '59х39x36 mm',
                'weight': '95,2 g',
                'location': 'Philippines',
                'img': 'ptb',
            }
        ]
    }


def index(request):
    return render(request, 'shop/index.html', context)


def product(request, num):
    product_id = request.path_info.split("/")[-1]
    shop_product = {}
    for value in context["products"]:
        if int(product_id) == value.get("id"):
            shop_product = value
            break
    print(shop_product)
    return render(request, 'products/products.html', shop_product)

