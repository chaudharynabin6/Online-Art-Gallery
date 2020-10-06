
from django.http import HttpResponse
from django.shortcuts import render
from utils.formating.table_format import dict_to_table

def home_view(request):
    user = request.user
    
    context = {
        "user" : user,
        "hello" : "hello"
    }
    dict_to_table(context)
    return render(request,"main/home.html",context)