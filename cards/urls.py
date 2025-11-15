from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('card/add/', views.add_card, name='add_card'),
    path('card/edit/<int:card_id>/', views.edit_card, name='edit_card'),
    path('card/delete/<int:card_id>/', views.delete_card, name='delete_card'),

    path('category/add/', views.add_category, name='add_category'),
    path('category/add/<int:parent_id>/', views.add_category, name='add_subcategory'),
    path('category/edit/<int:category_id>/', views.edit_category, name='edit_category'),
    path('category/delete/<int:category_id>/', views.delete_category, name='delete_category'),
]