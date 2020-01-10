from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
from .models import Prec
import csv
import sqlite3

def index(request) :
    # with open('C:/Users/admin/Documents/pansago/law_list_detail.csv', 'r', encoding='utf-8') as f:
    #     csv.field_size_limit(100000000)
    #     rdr = csv.reader(f)
    #     for line in rdr:
    #         law_no = line[0]
    #         law_title = line[1]
    #         law_event_no  = line[2]
    #         law_date	 = line[3]
    #         law_seongo  = line[4]
    #         law_court_name = line[5]
    #         law_event_type  = line[7]
    #         law_result   = line[9]
    #         law_content   = line[14]

    #         print(law_no)
                
    #         prec = Prec(law_no=law_no, law_title=law_title, law_event_no=law_event_no, law_date=law_date, law_seongo=law_seongo, law_court_name=law_court_name, law_event_type=law_event_type, law_result=law_result, law_content=law_content)
    #         prec.save()

    return render(request, 'index.html') ## templates 밑에 바로 읽음
    

def preclist(request) :
    if request.method == "GET":
        searchtype = request.GET.get('type','')
        searchkeyword = request.GET.get('text','')

        if searchtype =='law_court_name':
            precList = Prec.objects.filter(law_event_type__incontains=searchkeyword).order_by('law_event_type', '-law_date')

        elif searchtype =='law_title':
            precList = Prec.objects.filter(law_title__incontains=searchkeyword).order_by('law_title', '-law_date')

        if searchkeyword == '':
            precList = Prec.objects.raw('SELECT * FROM LAW_PREC ORDER BY LAW_DATE DESC')
        
        paginator = Paginator(precList, 20)
        page = request.GET.get('page')
        posts = paginator.get_page(page)    #페이지에 해당되는 값만
        pageList =[]

        for i in range(1, paginator.num_pages + 1, 1):
            pageList.append(i)

        return render(request, 'precList.html', {'precList' : precList, 'posts':posts, 'pageList':pageList, 'searchtype':searchtype, 'searchkeyword':searchkeyword})

        
        



