from django.urls import path
from django.contrib.auth import views as auth_views

from .views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('login/', login_request, name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('registration/', Registration.as_view(), name='registration'),
    path('profile/', Profile.as_view(), name='profile'),
    path('account/', account, name='account'),
    path("password_reset", password_reset_request, name="password_reset"),
    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html"),
         name='password_reset_confirm'),
    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
         name='password_reset_complete'),
    path('robots.txt', robots_txt),
    path('block/', block, name='block'),
    path('currency_rate/<str:currency1>/<str:currency2>/', Currency_rate.as_view(), name='block'),
    path('currencies/', currencies, name='currencies'),
    path('about/', about, name='about'),
    path('themes/', themes, name='themes'),
    path('ligth_theme/', ligth_theme, name='ligth_theme'),
    path('dark_theme/', dark_theme, name='dark_theme'),
]
