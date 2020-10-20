from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings

User = get_user_model()


class SocialPlatform(models.TextChoices):
    INSTAGRAM = 'instagram', 'Instagram'
    FACEBOOK = 'facebook', 'Facebook'
    TELEGRAM = 'telegram', 'Telegram'
    DISCORD = 'discord', 'Discord'


class Contact(models.Model):
    name = models.CharField(choices=SocialPlatform.choices, max_length=10)
    relevance = models.IntegerField(default=100)
    link = models.CharField(max_length=100, default='https://instagram.com/')

    @property
    def image(self):
        return f'{settings.MEDIA_URL}/img/contacts/{self.name}-256.png'

    objects = models.Manager()

    class Meta:
        ordering = ['-relevance']

    def __str__(self):
        return f'{self.name}'


class Testimonial(models.Model):
    """Testimonial displayed on the home page, to flex with new users and get more people"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    relevance = models.IntegerField(default=100)
    link = models.CharField(max_length=80, default='https://instagram.com/')
    display = models.BooleanField(default=True)

    class Meta:
        ordering = ['-relevance']

    objects = models.Manager()

    def __str__(self):
        return f'{self.user.username}-{self.relevance}-{self.display}'
