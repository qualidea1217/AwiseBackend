from django import forms
from .models import Survey


class survey_form(forms.ModelForm):
    class Meta:
        model = Survey
        fields = [
            'user_name',
            'year',
            'rent',
            'move_in_date',
            'num_of_rm',
            'location',
            'getup_time',
            'bed_time',
            'bring_people',
            'animal',
            'instrument',
            'clean',
            'cook',
            'share',
            'smoke',
            'alcohol'
        ]
