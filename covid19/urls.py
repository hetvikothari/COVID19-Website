from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('news/', views.news, name='news'),
    path('protect/', views.protect, name='protect'),
    path('doctors/', views.doctors, name='doctors'),
    path('cases/', views.cases, name='cases'),
]
