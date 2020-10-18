from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from PVLV_auth.views import register


urlpatterns = [
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path(
        'password-reset/',
        auth_views.PasswordResetView.as_view(
            template_name='registration/password-reset.html',
            success_url=reverse_lazy('password-reset-done')
        ),
        name='password-reset'
    ),
    path(
        'password-reset/done/',
        auth_views.PasswordResetDoneView.as_view(
            template_name='registration/password-reset-done.html'
        ),
        name='password-reset-done'
    ),
    path(
        'password-reset-confirm/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='registration/password-reset-confirm.html',
            success_url=reverse_lazy('password-reset-complete')
        ),
        name='password_reset_confirm'
    ),
    path(
        'password-reset-complete/',
        auth_views.PasswordResetCompleteView.as_view(
            template_name='registration/password-reset-complete.html'
        ),
        name='password-reset-complete'
    ),
]
