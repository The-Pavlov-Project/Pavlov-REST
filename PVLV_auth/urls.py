from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from PVLV_auth.views import register, activate
from .forms import UserLoginForm, UserPasswordResetForm, UserPasswordChangeForm


urlpatterns = [
    path('register/', register, name='register'),
    path('activate/<uidb64>/<token>/', activate, name='activate'),
    path(
        'login/',
        auth_views.LoginView.as_view(
            template_name='registration/login.html',
            authentication_form=UserLoginForm,
        ),
        name='login'
    ),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path(
        'password-reset/',
        auth_views.PasswordResetView.as_view(
            template_name='registration/password-reset.html',
            success_url=reverse_lazy('password-reset-done'),
            form_class=UserPasswordResetForm

        ),
        name='password-reset'
    ),
    path(
        'password-reset/done/',
        auth_views.PasswordResetDoneView.as_view(
            template_name='registration/password-reset-sent.html'
        ),
        name='password-reset-done'
    ),
    path(
        'password-change/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='registration/password-reset-update.html',
            success_url=reverse_lazy('password-reset-complete'),
            form_class=UserPasswordChangeForm
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
