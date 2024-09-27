from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'html/home.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'Name - {name}, phone - {phone}, message - {message}')
        return HttpResponse(f'Cпасибо, {name}, Ваше сообщение получено!')
    return render(request, 'html/contacts.html')