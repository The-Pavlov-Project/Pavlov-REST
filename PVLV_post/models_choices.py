from django.db import models


class Scope(models.TextChoices):
    POST = 'P', 'Post'
    SPOT = 'S', 'Spot'
    SPOT_M = 'SM', 'Spot Male'
    SPOT_F = 'SF', 'Spot Female'
    SPOT_C = 'SC', 'Spot Custom'


class TopImage(models.TextChoices):
    QM = 'quotation-marks', 'Quotation Marks'


class TextAlign(models.TextChoices):
    CENTER = 'center', 'Center'
    RIGHT = 'right', 'Right'
    LEFT = 'left', 'Left'


class LogoPosition(models.TextChoices):
    AUTO = 'auto', 'Auto'
    CENTER = 'center', 'Center'
    CENTER_UP = 'center-up', 'Center Up'
    CENTER_DOWN = 'center-down', 'Center Down'
    LEFT_UP = 'left-up', 'Left Up'
    LEFT_DOWN = 'left-down', 'Left Down'
    RIGHT_UP = 'right-up', 'Right Up'
    RIGHT_DOWN = 'right-down', 'Right Down'


class Rectangle(models.TextChoices):
    T1 = 'tick_1', 'Tick 1'
