from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
    return render(request, 'index.html')

def search(request):
    if request.method == 'POST':
        searched = request.POST['searched']        
        corp_infos = CorpInfo.objects.filter(stock_name=searched)

        positive = positive_prev1 = positive_prev2 = positive_prev3 = 100
        negative = negative_prev1 = negative_prev2 = negative_prev3 = 0
        if corp_infos:
            for corp_info in corp_infos:
                if corp_info.sentiment_analysis_ratio:
                    positive = int(corp_info.sentiment_analysis_ratio * 100)
                    negative = 100 - positive

                    positive_prev1 = int(corp_info.sentiment_analysis_ratio_prev_1 * 100)
                    negative_prev1 = 100 - positive_prev1
                    positive_prev2 = int(corp_info.sentiment_analysis_ratio_prev_2 * 100)
                    negative_prev2 = 100 - positive_prev2
                    positive_prev3 = int(corp_info.sentiment_analysis_ratio_prev_3 * 100)
                    negative_prev3 = 100 - positive_prev3

                    # positive = corp_info.sentiment_analysis_ratio
                    # negative = 100 - positive

                    # positive_prev1 = corp_info.sentiment_analysis_ratio_prev_1
                    # negative_prev1 = 100 - positive_prev1
                    # positive_prev2 = corp_info.sentiment_analysis_ratio_prev_2
                    # negative_prev2 = 100 - positive_prev2
                    # positive_prev3 = corp_info.sentiment_analysis_ratio_prev_3
                    # negative_prev3 = 100 - positive_prev3
                
        return render(request, 'searched.html', {'searched': searched, 'corp_infos': corp_infos, 'positive': positive, 'negative': negative, 'positive_prev1': positive_prev1, 'positive_prev2': positive_prev2, 'positive_prev3': positive_prev3,})
    else:
        return render(request, 'searched.html', {})