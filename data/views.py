from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def student(request):
    return HttpResponse ("นักเรียน")

def add_stu(request, id):
    return HttpResponse ("เพิ่มนร.")

def edit_stu(request):
    return HttpResponse ("แก้ไขข้อมูลนร.")
    
def order(request, id):
    return HttpResponse ("วิชาเรียน")

def add_sub(request):
    return HttpResponse ("เพิ่มวิชาเรียน")

def edit_sub(request):
    return HttpResponse ("แก้วิชาเรียน")
