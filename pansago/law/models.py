from django.db import models

class Prec(models.Model):
    objects     = models.Manager()  #VS code오류 제거용
    law_index   = models.AutoField(primary_key=True)	
    law_no 		= models.IntegerField()                   #판례정보 일련번호
    law_title	= models.CharField(max_length=200)	                #사건명
    law_event_no = models.IntegerField()	                #사건번호
    law_date	= models.DateTimeField()	                #선고일자
    law_seongo	 = models.CharField(max_length=200)                   #선고
    law_court_name = models.CharField(max_length=200)	                #법원명
    law_court_code = models.IntegerField()	                #법원종류코드
    law_event_type = models.CharField(max_length=200)	                #사건종류명
    law_event_code = models.IntegerField()	                #사건종류코드
    law_result	= models.CharField(max_length=50)             #판결유형
    law_judge	= models.CharField(max_length=200)                    #판시사항
    law_judge_summary  =  models.CharField(max_length=300)               #판결요지
    law_ref	= models.CharField(max_length=200)	                    #참조조문
    law_ref_precedent  = models.CharField(max_length=200)	    #참조판례
    law_content  = models.TextField()	                #판례내용
    
    def __str__(self):
        return (self.law_index) #문자만 가능