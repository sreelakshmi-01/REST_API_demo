from django.urls import path
from app1 import views

urlpatterns = [
    path('all/', views.electronics_all),
    path('add', views.add_product),
    path('electronics/<int:electronic_id>/', views.electronics_one),
    path('electronics_del/<int:electronic_id>', views.del_electronics),
    path('electronics_upd/<int:electronic_id>', views.electronic_update),
]