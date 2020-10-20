from django.shortcuts import render
from django.contrib.auth import get_user_model
from .models import Contact, Testimonial

User = get_user_model()


def home(request):
    contacts = Contact.objects.all()

    context = {
        'contacts': Contact.objects.all(),
        'testimonials': Testimonial.objects.filter(display=True).order_by('-relevance'),
    }
    return render(request, 'home.html', context)
