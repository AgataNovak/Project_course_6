from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from catalog.models import Category, Product

#
# def home(request):
#     return render(request, 'html/home.html')
#
#
# def contacts(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         phone = request.POST.get('phone')
#         message = request.POST.get('message')
#         print(f'Name - {name}, phone - {phone}, message - {message}')
#         return HttpResponse(f'Cпасибо, {name}, Ваше сообщение получено!')
#     return render(request, 'html/contacts.html')


def product_list(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'html/products_list.html', context)


def product_details(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {'product': product}
    return render(request, 'html/product_details.html', context)


def contacts(request):
    return render(request, 'html/contacts.html')
