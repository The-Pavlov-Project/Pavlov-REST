from django.db import models
from .models_choices import TopImage, TextAlign, LogoPosition
from django.contrib.auth import get_user_model

User = get_user_model()


class Color(models.Model):

    background = models.CharField(max_length=7)
    primary = models.CharField(max_length=7)
    text = models.CharField(max_length=7)

    class Meta:
        ordering = []

    objects = models.Manager()

    def __str__(self):
        return f'{self.background, self.primary, self.text}'


class PostGeneratorSubConfig(models.Model):

    colors = models.ManyToManyField(Color, related_name='colors')

    logo = models.CharField(default='img/icons/pavlov.png', max_length=30)
    colorize_logo = models.BooleanField(default=False)

    top_image = models.CharField(choices=TopImage.choices, max_length=20)
    text_align = models.CharField(choices=TextAlign.choices, max_length=20)
    logo_position = models.CharField(choices=LogoPosition.choices, max_length=20)
    rectangle = models.CharField(choices=LogoPosition.choices, max_length=20)

    image_scale = models.CharField(default='1:1', max_length=20)

    def __str__(self):
        return f'{self.logo}'


class PostGeneratorConfig(models.Model):

    owners = models.ManyToManyField(
        User
    )

    name = models.CharField(max_length=20, null=False)

    post = models.ForeignKey(PostGeneratorSubConfig, null=True, on_delete=models.SET_NULL, related_name='post')
    spot = models.ForeignKey(PostGeneratorSubConfig, null=True, on_delete=models.SET_NULL, related_name='spot')

    class Meta:
        ordering = []

    objects = models.Manager()

    def __str__(self):
        return f'{self.name}'
