from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/', views.student),
    path('add_stu/', views.add_stu),
    path('esit_stu/', views.edit_stu),
    path('order/', admin.order),
    path('add_sub/', views.add_sup),
    path('edit_sub/', views.edit_sub)
]