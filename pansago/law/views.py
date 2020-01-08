from django.shortcuts import render

# Create your views here.

def index(request) :
    return render(request, 'index.html') ## templates 밑에 바로 읽음
    