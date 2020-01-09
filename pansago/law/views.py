from django.shortcuts import render
# Create your views here.
from .models import Prec
import csv

def index(request) :
    with open('C:/Users/admin/Documents/pansago/law_list_detail.csv', 'r', encoding='utf-8') as f:
        rdr = csv.reader(f)
        
        for line in rdr:
            law_no = line[0]

            print(law_no)

            law_title = line[1]
            law_event_no  = line[2]
            law_date	 = line[3]
            law_seongo  = line[4]
            law_court_name = line[5]
            law_court_code   = line[6]
            law_event_type  = line[7]
            law_event_code = line[8]
            law_result   = line[9]
            law_judge    = line[10]
            law_judge_summary   = line[11]
            law_ref   = line[12]
            law_ref_precedent  = line[13]
            law_content   = line[14]
                
            prec = Prec(law_no=law_no, law_title=law_title, law_event_no=law_event_no, law_date=law_date, law_seongo=law_seongo, law_court_name=law_court_name, law_court_code=law_court_code, law_event_type=law_event_type, law_event_code=law_event_code, law_result=law_result, law_judge= law_judge, law_judge_summary= law_judge_summary, law_ref=law_ref, law_ref_precedent=law_ref_precedent, law_content=law_content)
            prec.save()

    return render(request, 'index.html') ## templates 밑에 바로 읽음
    
