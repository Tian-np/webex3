from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def login(request):
    return HttpResponse ("หน้าจอ login")

def detail(request, id):
    return HttpResponse ("ID : %s" % id)

def checks(request):
    return HttpResponse ("QR code")
