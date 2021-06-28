from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('new_search', views.new_search, name='new_search'),
    path('contact', views.contact, name='contact'),

]