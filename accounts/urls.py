from django.urls import path
from django.contrib.auth import views as auth_views
from.import views
urlpatterns = [
    path('',views.index,name='index'),
    path('home/',views.home,name='home'),
    path('register/', views.register_view, name='register'),
    path('order/', views.order_food, name='order_food'),
   
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),

    # path('home/',views.index,name='index')
     path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset.html'), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
]
