import json

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from home.forms import SearchForm
from home.models import Setting
from product.models import Category, Product, Images, Comment


def index(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    products_slider = Product.objects.all().order_by('id')[:4]
    products_latest = Product.objects.all().order_by('-id')[:4]
    products_picked = Product.objects.all().order_by('?')[:4]
    page = "home"
    context = {'setting': setting,
               'page': page,
               'category': category,
               'products_slider': products_slider,
               'products_latest': products_latest,
               'products_picked': products_picked,
               }
    return render(request, 'index.html', context)


def aboutus(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    context = {'setting': setting, 'category': category
     }

    return render(request, 'about.html', context)


def contactus(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    context = {'setting': setting, 'category': category,
    }

    return render(request, 'contact.html', context)


def category_products(request, id, slug):
    category = Category.objects.all()
    products = Product.objects.filter(category_id=id)
    context = {'products': products,
               'category': category,
               }
    return render(request, 'category_products.html', context)


def search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            catid = form.cleaned_data['catid']
            if catid == 0:
                products = Product.objects.filter(name__icontains=query)
            else:
                products = Product.objects.filter(name__icontains=query, category_id=catid)

            cateory = Category.objects.all()
            context = {
                'products': products,
                'category': cateory,
                'query': query,
            }
            return render(request, 'search_products.html', context)
    return HttpResponseRedirect('/')


def search_auto(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        products = Product.objects.filter(name__icontains=q)
        results = []
        for rs in products:
            products_json = {}
            products_json = rs.name
            results.append(products_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)


def product_detail(request, id, slug):
    category = Category.objects.all()
    product = Product.objects.get(pk=id)
    images = Images.objects.filter(product_id=id)
    comment = Comment.objects.filter(product_id=id, status="True")
    stars = 0
    count = 0
    for i in comment:
        stars += i.rate
        count += 1
    if count > 0:
        stars = stars/count
    context = {'product': product,
               'category': category,
               'images': images,
               'comments': comment,
               'stars': stars,
               'count': count,
               }
    return render(request, 'product_detail.html', context)
