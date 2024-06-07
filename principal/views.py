from django.shortcuts import render

def home(request):
    return render(request, 'principal/home.html')

def about(request):
    return render(request, 'principal/about.html')

def contact(request):
    return render(request, 'principal/contact.html')
