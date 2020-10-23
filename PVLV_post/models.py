from django.db import models
from django.contrib.auth import get_user_model
from PIL import Image


User = get_user_model()
LOGO_DEFAULT = 'default/post.png'


class Scope(models.TextChoices):
    POST = 'P', 'Post'
    SPOT = 'S', 'Spot'
    SPOT_M = 'SM', 'Spot Male'
    SPOT_F = 'SF', 'Spot Female'
    SPOT_C = 'SC', 'Spot Custom'


class ColorizeLogo(models.TextChoices):
    FALSE = 'false', 'Disabled'
    DARK_LIGHT = 'DL', 'Dark and Light'
    TRUE = 'true', 'True'


class ScopeImage(models.TextChoices):
    NONE = 'none', 'Disabled'
    QM = 'quotation-marks', 'Quotation Marks'


class TextAlign(models.TextChoices):
    CENTER = 'center', 'Center'
    RIGHT = 'right', 'Right'
    LEFT = 'left', 'Left'


class LogoPosition(models.TextChoices):
    NONE = 'none', 'Disabled'
    AUTO = 'auto', 'Auto'
    CENTER = 'center', 'Center'
    CENTER_UP = 'center-up', 'Center Up'
    CENTER_DOWN = 'center-down', 'Center Down'
    LEFT_UP = 'left-up', 'Left Up'
    LEFT_DOWN = 'left-down', 'Left Down'
    RIGHT_UP = 'right-up', 'Right Up'
    RIGHT_DOWN = 'right-down', 'Right Down'


class Rectangle(models.TextChoices):
    NONE = 'none', 'Disabled'
    T1 = 'tick_1', 'Tick 1'


class Color(models.Model):

    background = models.CharField(max_length=7)
    primary = models.CharField(max_length=7)
    text = models.CharField(max_length=7)

    class Meta:
        ordering = []

    objects = models.Manager()

    def __str__(self):
        return f'{self.background, self.primary, self.text}'


class PostGeneratorConfig(models.Model):

    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')

    operators = models.ManyToManyField(
        User,
        related_name='operators'
    )

    # for which command have to be used (.post, .spot etc)
    scope = models.CharField(choices=Scope.choices, default=Scope.POST, max_length=30)

    # colors set for the post
    colors = models.ManyToManyField(Color, related_name='colors')

    logo = models.ImageField(default=LOGO_DEFAULT, upload_to='post')
    logo_position = models.CharField(choices=LogoPosition.choices, default=LogoPosition.CENTER, max_length=20)
    colorize_logo = models.CharField(choices=ColorizeLogo.choices, default=ColorizeLogo.FALSE, max_length=20)

    # the image over the text for characterization
    scope_image = models.CharField(choices=ScopeImage.choices, default=ScopeImage.NONE, max_length=20)
    text_align = models.CharField(choices=TextAlign.choices, default=TextAlign.CENTER, max_length=20)
    rectangle = models.CharField(choices=Rectangle.choices, default=Rectangle.NONE, max_length=20)

    # for the post with only images, or a background image
    image_scale = models.CharField(default='1:1', max_length=20)

    class Meta:
        ordering = ['scope']
        unique_together = ('owner', 'scope')

    objects = models.Manager()

    def __str__(self):
        return f'{self.owner}-{self.scope}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.logo.path)

        dim = 1024  # the image square resize dimension

        if img.height > dim or img.width > dim:
            output_size = (dim, dim)
            img.thumbnail(output_size)
            img.save(self.logo.path)
