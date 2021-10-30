from django.contrib import admin
from django.urls import path,include
from.views import page_1,page_2,page_3

urlpatterns = [
    path('1',page_1),
    path('2', page_2),
    path('3', page_3),

]