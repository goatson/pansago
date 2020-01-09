from django.shortcuts import render
from .models import Prec
import csv

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

    return render(request, 'index.html')