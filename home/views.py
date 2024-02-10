from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
    return render(request, 'index.html')

def search(request):
    if request.method == 'POST':
        searched = request.POST['searched']        
        company_infos = CompanyInfo.objects.filter(company_name=searched)
        return render(request, 'searched.html', {'searched': searched, 'company_infos': company_infos})
    else:
        return render(request, 'searched.html', {})

# def search(request):
#     if request.method == 'POST':
#         searched = request.POST['searched']        
#         # recipes = Recipe.objects.filter(name__contains=searched)
#         return render(request, 'searched.html', {'searched': searched})
#     else:
#         return render(request, 'searched.html', {'searched': searched})