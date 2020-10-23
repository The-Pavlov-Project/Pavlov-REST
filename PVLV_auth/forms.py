from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field, Row, Column
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm, PasswordChangeForm

User = get_user_model()


class UserLoginForm(AuthenticationForm):

    class Meta:
        model = User
        fields = ['username', 'password']

    helper = FormHelper()
    helper.form_class = 'user'
    helper.form_show_labels = False
    helper.layout = Layout(
        Field('username', placeholder="Username", css_class='form-control-user'),
        Field('password', placeholder="Password", css_class='form-control-user'),
        Submit('Log in', 'Register Account', css_class='btn btn-primary btn-user btn-block'),
    )


class UserRegisterForm(UserCreationForm):

    email = forms.EmailField()
    password1 = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {
            'username': None,
        }

    helper = FormHelper()
    helper.form_class = 'user'
    helper.form_show_labels = False
    helper.layout = Layout(
        Field('username', placeholder="Username", css_class='form-control-user'),
        Field('email', placeholder="Email", css_class='form-control-user'),
        Row(
            Column(
                Field('password1', placeholder="Password", css_class='form-control-user'),
                css_class='col-sm-6 mb-3 mb-sm-0'
            ),
            Column(
                Field('password2', placeholder="Confirm password", css_class='form-control-user'),
                css_class='col-sm-6'
            ),
        ),
        Submit('Log in', 'Register Account', css_class='btn btn-primary btn-user btn-block'),
    )


class UserPasswordResetForm(PasswordResetForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['email']

    helper = FormHelper()
    helper.form_class = 'user'
    helper.form_show_labels = False
    helper.layout = Layout(
        Field('email', placeholder="Enter email address...", css_class='form-control-user'),
        Submit('Log in', 'Reset Password', css_class='btn btn-primary btn-user btn-block'),
    )


class UserPasswordChangeForm(PasswordChangeForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']

    helper = FormHelper()
    helper.form_class = 'user'
    helper.form_show_labels = False
    helper.layout = Layout(
        Field('new_password1', placeholder="New password", css_class='form-control-user'),
        Field('new_password2', placeholder="New password again", css_class='form-control-user'),
        Submit('submit', 'Reset Password', css_class='btn btn-primary btn-user btn-block'),
    )


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'image']
