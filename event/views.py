

from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def event(request):
    return render(request,"event/event.html")

@login_required(login_url='login')
def event_details(request):
    return render(request,"event/event_details.html")
