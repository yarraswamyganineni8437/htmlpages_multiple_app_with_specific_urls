from django.urls import path
from app2.views import *
app_name='nothing'

urlpatterns=[
    path('sample/',sample,name='sample'),
    path('sample2/',sample2,name='sample2'),
]