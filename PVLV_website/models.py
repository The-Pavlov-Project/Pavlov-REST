from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Testimonial(models.Model):
    """Testimonial displayed on the home page, to flex with new users and get more people"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, unique=True)
    relevance = models.IntegerField(default=100)
    display = models.BooleanField(default=True)

    class Meta:
        ordering = ['-relevance']

    objects = models.Manager()

    def __str__(self):
        return f'{self.user.username}-{self.relevance}-{self.display}'
