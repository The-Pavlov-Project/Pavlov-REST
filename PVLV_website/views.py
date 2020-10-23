from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from .models import Contact, Testimonial

User = get_user_model()


def home(request):

    context = {
        'contacts': Contact.objects.all(),
        'testimonials': Testimonial.objects.filter(display=True).order_by('-relevance'),
    }
    return render(request, 'home.html', context)


@login_required
def dashboard(request):
    context = {}
    return render(request, 'console/dashboard.html', context)
