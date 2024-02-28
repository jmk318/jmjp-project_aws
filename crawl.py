import os
import sys
import urllib.request
import datetime
import time
import json

client_id = '9pSa1C5Lj0Yy8_Pd3mn3'
client_secret = '88ZTtceaKm'
dir_path = '/home/ec2-user/environment'

#[CODE 1]
def getRequestUrl(url):
    req = urllib.request.Request(url)
    req.add_header("X-Naver-Client-Id", client_id)
    req.add_header("X-Naver-Client-Secret", client_secret)
    
    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print("[%s]Url Request Success" % datetime.datetime.now())
            return response.read().decode('utf-8')
    except Exception as e :
        print(e)
        print("[%s] Error for URL : %s" % (datetime.datetime.now(), url))
        return None

#[CODE 2]
def getNaverSearch(node, srcText, start, display):
    base = "https://openapi.naver.com/v1/search"
    node = "/%s.json" % node
    parameters = "?query=%s&start=%s&display=%s" % (urllib.parse.quote(srcText), start, display)

    url = base + node + parameters
    responseDecode = getRequestUrl(url)     #[CODE 1]

    if(responseDecode == None):
        return None
    else:
        return json.loads(responseDecode)

#[CODE 3]
def getPostData(post, jsonResult, cnt):
    title = post['title']
    jsonResult.append({'cnt':cnt, 'title':title})
    return

#[CODE 0]
def main():
    node = 'news'  # 크롤링 대상
    companies = ['삼성전자', 'HMM', '현대차', '기아', '신한지주', 'KB금융', '하나금융지주', 'POSCO홀딩스' '우리금융지주', '기업은행',
                 '현대모비스', 'SK하이닉스', 'GS', 'S-Oil', '삼성물산', 'LG', '삼성SDI', 'LG화학', '대한항공', '삼성생명',
                 'SK이노베이션', '한국가스공사', 'HD현대', '카카오', '한화', '삼성화재', 'KT', 'LG전자', '현대글로비스', '삼성에스디에스',
                 'SK', '메리츠금융지주', '이마트', '금호석유', '현대제철', 'KT&G', 'DB손해보험', '삼성전기', 'LG이노텍', 'SK텔레콤',
                 '에스디바이오센서', 'OCI 홀딩스', 'BNK금융지주', '삼성바이오로직스', '고려아연', 'LG에너지솔루션', 'NAVER', '한화생명', '한국타이어앤테크놀로지',
                 '한진칼', '팬오션', '영원무역', '삼성엔지니어링', 'LG유플러스', '두산밥캣', '미래에셋증권', '한국금융지주', '삼성카드', 'JB금융지주', 'CJ제일제당',
                 '포스코인터내셔널', '현대해상', 'DB하이텍', '셀트리온', 'KG스틸', 'LX인터내셔널', '키움증권', '대우건설', '크래프톤', 'KG ETS',
                 '코웨이', 'LS', 'F&F', '영원무역홀딩스', '엔씨소프트', 'SK디스커버리', '삼성증권', 'DL이앤씨', '동국홀딩스', '현대건설',
                 '신세계', 'DGB금융지주', '오리온', '다우기술', '영풍', '한화솔루션', '엑세스바이오', '휠라홀딩스', '태광산업', 'GS건설',
                 '그래디언트', '바이오노트', 'KG케미칼', 'NH투자증권', '세아제강지주', '티케이케미칼', '오뚜기', '엘앤에프', '카카오뱅크', 'SK스퀘어']

    for srcText in companies:
        cnt = 0
        jsonResult = []
        
        jsonResponse = getNaverSearch(node, srcText, 1, 100)  #[CODE 2]
        total = jsonResponse['total']
        
        while((jsonResponse != None) and (jsonResponse['display'] != 0)):
            for post in jsonResponse['items']:
                cnt+= 1
                getPostData(post, jsonResult, cnt)   #[CODE 3]
                
            start = jsonResponse['start'] + jsonResponse['display']
            if start > 100:
                break
            jsonResponse = getNaverSearch(node, srcText, start, 100)   #[CODE 2]
            
        print('전체 검색 : %d 건' %total)
            
        with open(os.path.join(dir_path, '%s_naver_%s.json' % (srcText, node)), 'w', encoding='utf8') as outfile:
            jsonFile = json.dumps(jsonResult, indent=4, sort_keys = True, ensure_ascii = False)
                
            outfile.write(jsonFile)
                
        print("가져온 데이터 : %d 건" %(cnt))
        print('%s_naver_%s.json SAVED' % (srcText, node))

if __name__ == '__main__':
    main()
