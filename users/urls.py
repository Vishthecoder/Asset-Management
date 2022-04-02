from django.urls import path
from .views import edit, dashboard, register
from django.urls import reverse_lazy
from django.contrib.auth.views import (LoginView, LogoutView, PasswordResetDoneView, PasswordResetView,
                                       PasswordResetCompleteView, PasswordResetConfirmView,
                                       PasswordChangeView, PasswordChangeDoneView,
                                       PasswordResetDoneView)



urlpatterns = [
    path('register/', register, name='register'),
    path('edit/', edit, name='edit'),
    path('', dashboard, name='dashboard'),
    path('login/', LoginView.as_view(template_name='asset/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='usersapp/logged_out.html'), name='logout'),
    path('password_change/', PasswordChangeView.as_view(
        template_name='usersapp/password_change_form.html'), name='password_change'),
    path('password_change/done/', PasswordChangeDoneView.as_view(template_name='usersapp/password_change_done.html'),
         name='password_change_done'),
    path('password_reset/', PasswordResetView.as_view(
        template_name='usersapp/password_reset_form.html',
        email_template_name='usersapp/password_reset_email.html',
        success_url=reverse_lazy('password_reset_done')), name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(
        template_name='usersapp/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
        template_name='usersapp/password_reset_confirm.html',
        success_url=reverse_lazy('login')), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(
        template_name='usersapp/password_reset_complete.html'), name='password_reset_complete'),

]