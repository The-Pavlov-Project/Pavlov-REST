from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from .utils import TokenGenerator
from .forms import UserRegisterForm

User = get_user_model()


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            current_site = get_current_site(request)
            body = render_to_string(
                'mail/activate.html',
                {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': TokenGenerator().make_token(user)
                }
            )
            email_message = EmailMessage(
                subject=f'{user.username} activate your account',
                body=body,
                to=[user.email],
                headers={'Message-ID': 'foo'},
            )
            email_message.send()
            messages.success(request, f'Your account has been created! Verify your account, we have sent you an email')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {'form': form})


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except User.DoesNotExist:
        user = None
    if user and TokenGenerator().check_token(user, token):
        user.is_verified = True
        user.save()
        messages.success(request, 'Account verified successfully')
        return redirect('login')

    messages.error(request, f'Something went wrong login and require a new activation link')
    return redirect('profile')
