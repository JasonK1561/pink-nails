from django.contrib import admin
from django.urls import path, include
from Pink_Nails_App import views

app_name = 'pink_nails'

urlpatterns = [
    path('contact/', views.ContactTemplateView.as_view(), name='contact'),
    path('services/', views.ServicesTemplateView.as_view(), name='service'),
]
