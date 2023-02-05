from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.formprocess, name='formprocess'),
    # path('result/', views.formprocess, name='formprocess'),
]