from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def staffs(request):
    return render(request, 'main/staffs.html')


def contact(request):
    return render(request, 'main/contact.html')
