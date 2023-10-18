from django.shortcuts import render

# Create your views here.

def catt(request):
    return render(request, 'index.html')