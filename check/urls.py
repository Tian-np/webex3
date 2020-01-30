from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login),
    path('detail/<int:id>/', views.detail),
    path('checks/', views.checks)
]