from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login_page/', views.login_page, name='login_page'),
    path('logout_page/', views.logout_page, name='logout_page'),
    path('signup_page/', views.signup_page, name='signup_page'),
    path('user_profile/', views.user_profile, name='user_profile'),
]
