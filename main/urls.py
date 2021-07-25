from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.user_login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup', views.signup, name='signup'),



    path('password_change', auth_views.PasswordChangeView.as_view(
        template_name="password_change.html"), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(
        template_name="password_change_done.html"), name='password_change_done'),



    path('password_reset/', auth_views.PasswordResetView.as_view(template_name="password_reset.html"),
         name='password_reset'),
    path('password_reset_done', auth_views.PasswordResetDoneView.as_view(template_name="password_reset_done.html"),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html"),
         name='password_reset_confirm'),
    path('password_reset_complete', auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_complete.html"),
         name='password_reset_complete')
]
