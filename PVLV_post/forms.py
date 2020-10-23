from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field
from .models import (
    PostGeneratorConfig,
    Scope,
    LogoPosition,
    ColorizeLogo,
    ScopeImage,
    TextAlign,
    Rectangle,
)


class PostForm(forms.ModelForm):

    scope = forms.ChoiceField(choices=Scope.choices, required=False)
    logo = forms.ImageField(required=False)
    logo_position = forms.ChoiceField(choices=LogoPosition.choices, required=False)
    colorize_logo = forms.ChoiceField(
        choices=ColorizeLogo.choices,
        required=False,
        label='Automatically change the color of the logo to match with current post color'
    )
    top_image = forms.ChoiceField(
        choices=ScopeImage.choices,
        required=False,
        label='Set the image on top of the text'
    )
    text_align = forms.ChoiceField(choices=TextAlign.choices, required=False)
    rectangle = forms.ChoiceField(
        choices=Rectangle.choices,
        required=False,
        label='Outline of the post'
    )

    class Meta:
        model = PostGeneratorConfig
        fields = [
            'logo',
            'logo_position',
            'colorize_logo',
            'top_image',
            'text_align',
            'rectangle'
            ]

    helper = FormHelper()
    helper.layout = Layout(
        Field('logo'),
        Field('logo_position'),
        Field('colorize_logo'),
        Field('top_image'),
        Field('text_align'),
        Field('rectangle'),
        Submit('submit', 'Save'),
    )
