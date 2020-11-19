from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'result/add_result.html')

def view_result(request):
    return render(request,'result/view_result.html')

def display_result(request):
    return render(request, 'result/display_result.html')