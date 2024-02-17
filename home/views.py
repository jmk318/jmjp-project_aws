from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
    return render(request, 'index.html')

def search(request):
    if request.method == 'POST':
        searched = request.POST['searched']        
        corp_infos = CorpInfo.objects.filter(stock_name=searched)
        balance_sheets = Top500.objects.filter(종목명=searched)
        return render(request, 'searched.html', {'searched': searched, 'corp_infos': corp_infos, 'balance_sheets': balance_sheets})
    else:
        return render(request, 'searched.html', {})