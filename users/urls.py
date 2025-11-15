from django.urls import path
from .views import logout_view, create_admin
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('create-admin/', create_admin),
]
