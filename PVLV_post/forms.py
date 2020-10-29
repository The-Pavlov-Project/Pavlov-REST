from crispy_forms.helper import FormHelper
from django import forms
from django.forms.models import inlineformset_factory
from .models import (
    Post,
    GeneratorSetting,
    Platform,
    PlatformType
)


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = []


class GeneratorSettingForm(forms.ModelForm):

    class Meta:
        model = GeneratorSetting
        fields = [
            'scope',
            'display_name_tag',
            'colors',
            'logo',
            'logo_position',
            'colorize_logo',
            'scope_image',
            'text_align',
            'line_position',
            'rectangle',
            ]
        labels = {
            'colorize_logo': 'Automatically change the color of the logo to match with current post color',
            'scope_image': 'Set the image on top of the text',
            'rectangle': 'Outline of the post',
        }

    def __init__(self, *args, **kwargs):

        super(GeneratorSettingForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3 create-label'
        self.helper.field_class = 'col-md-9'


class PlatformForm(forms.ModelForm):

    # add the default void value in selection
    platforms = [(u'', u'---')]
    platforms.extend(PlatformType.choices)

    platform = forms.ChoiceField(choices=platforms)

    class Meta:
        model = Platform
        fields = ['platform', 'name_tag']

    def __init__(self, *args, **kwargs):
        super(PlatformForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3 create-label'
        self.helper.field_class = 'col-md-9'


GeneratorSettingsInlineFormSet = inlineformset_factory(
        Post,
        GeneratorSetting,
        form=GeneratorSettingForm,
        max_num=5,
        extra=1,
        can_delete=True,
    )


PlatformInlineFormSet = inlineformset_factory(
        Post,
        Platform,
        form=PlatformForm,
        max_num=2,
        extra=1,
        can_delete=True,
    )
