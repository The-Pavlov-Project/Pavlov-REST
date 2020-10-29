from django.db import models
from django.contrib.auth import get_user_model
from PIL import Image


User = get_user_model()
LOGO_DEFAULT = 'default/post.png'


class PlatformType(models.TextChoices):
    INSTAGRAM = 'INSTAGRAM', 'Instagram'
    TWITTER = 'TWITTER', 'Twitter'


class Scope(models.TextChoices):
    POST = 'P', 'Post'
    SPOT = 'S', 'Spot'
    SPOT_M = 'SM', 'Spot Male'
    SPOT_F = 'SF', 'Spot Female'
    SPOT_C = 'SC', 'Spot Custom'


class DisplayNameTag(models.TextChoices):
    TRUE = 'T', 'True'
    USERNAME = 'U', 'Username'
    NONE = 'N', 'Disabled'


class ColorizeLogo(models.TextChoices):
    FALSE = None, 'Disabled'
    DARK_LIGHT = 'dl', 'Dark and Light'
    TRUE = 'true', 'True'


class ScopeImage(models.TextChoices):
    NONE = None, 'Disabled'
    QM = 'quotation-marks', 'Quotation Marks'


class TextAlign(models.TextChoices):
    CENTER = 'center', 'Center'
    RIGHT = 'right', 'Right'
    LEFT = 'left', 'Left'


class LinePosition(models.TextChoices):
    NONE = None, 'Disabled'
    CENTER = 'center', 'Center'
    RIGHT = 'right', 'Right'
    LEFT = 'left', 'Left'


class LogoPosition(models.TextChoices):
    NONE = None, 'Disabled'
    AUTO = 'auto', 'Auto'
    CENTER = 'center', 'Center'
    CENTER_UP = 'center-up', 'Center Up'
    CENTER_DOWN = 'center-down', 'Center Down'
    LEFT_UP = 'left-up', 'Left Up'
    LEFT_DOWN = 'left-down', 'Left Down'
    RIGHT_UP = 'right-up', 'Right Up'
    RIGHT_DOWN = 'right-down', 'Right Down'


class Rectangle(models.TextChoices):
    NONE = None, 'Disabled'
    T1 = 'tick-1', 'Tick 1'


class Post(models.Model):
    """main obj of the post structure"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='owner')

    operators = models.ManyToManyField(
        User,
        related_name='operators'
    )

    # main_logo = models.ImageField(default=LOGO_DEFAULT, upload_to='post')

    def __repr__(self):
        return f'{self.user}'

    def __str__(self):
        return f'{self.user}'


class Color(models.Model):
    """save the colors as a default set in hex value"""
    background = models.CharField(max_length=7)
    primary = models.CharField(max_length=7)
    text = models.CharField(max_length=7)

    @property
    def is_dark(self):
        """calculate if the color is dark, for the auto text and logo colorization"""
        value = self.background.lstrip('#')
        lv = len(value)
        rgb = tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))
        luma = 0.2126 * rgb[0] + 0.7152 * rgb[1] + 0.0722 * rgb[2]
        if luma < 40:
            return True
        return False

    objects = models.Manager()

    def __str__(self):
        return f'{self.background, self.primary, self.text}'


class GeneratorSetting(models.Model):

    parent = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='settings')
    # for which command have to be used (.post, .spot etc)
    scope = models.CharField(max_length=30)

    # if the name tag should be displayed in the post
    display_name_tag = models.CharField(choices=DisplayNameTag.choices, default=DisplayNameTag.USERNAME, max_length=20)

    # colors set for the post
    colors = models.ManyToManyField(Color, related_name='colors')

    # operations on the logo, the logo can be changed locally
    logo = models.ImageField(default=LOGO_DEFAULT, upload_to='post')
    logo_position = models.CharField(choices=LogoPosition.choices, default=LogoPosition.CENTER, max_length=20)
    colorize_logo = models.CharField(choices=ColorizeLogo.choices, default=ColorizeLogo.FALSE, max_length=20)

    # the image over the text for characterization
    scope_image = models.CharField(choices=ScopeImage.choices, default=ScopeImage.NONE, max_length=20)

    # where to align the text
    text_align = models.CharField(choices=TextAlign.choices, default=TextAlign.CENTER, max_length=20)
    line_position = models.CharField(choices=LinePosition.choices, default=LinePosition.CENTER, max_length=20)

    # display the rectangle delimitation border
    rectangle = models.CharField(choices=Rectangle.choices, default=Rectangle.NONE, max_length=20)

    # for the post with only images, or a background image
    image_scale = models.CharField(default='1:1', max_length=20)

    class Meta:
        ordering = ['scope']
        unique_together = ('parent', 'scope')

    objects = models.Manager()

    def __str__(self):
        return f'{self.parent}-{self.scope}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.logo.path)

        dim = 1024  # the image square resize dimension

        if img.height > dim or img.width > dim:
            output_size = (dim, dim)
            img.thumbnail(output_size)
            img.save(self.logo.path)


class Platform(models.Model):
    """
    The platform for which the post is generated for
    Must specify info such name-tag of the page
    """
    parent = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='platforms')
    platform = models.CharField(choices=PlatformType.choices, default=PlatformType.INSTAGRAM, max_length=30)

    # the username at the end of the post
    name_tag = models.CharField(default='@name_tag', max_length=30)

    objects = models.Manager()

    class Meta:
        unique_together = ('parent', 'platform')

    def __str__(self):
        return f'{self.parent}-{self.platform}'
