from django.urls import path
from app1 import views

urlpatterns = [
    path('all/', views.electronics_all),
    path('add', views.add_product),
    path('electronics/<int:electronic_id>/', views.electronics_one),
]