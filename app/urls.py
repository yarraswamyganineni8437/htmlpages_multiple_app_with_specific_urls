from django.urls import path
from app.views import *
app_name='something'

urlpatterns=[
    path('sample/',sample,name='sample'),
    path('sample1/',sample1,name='sample1'),
]