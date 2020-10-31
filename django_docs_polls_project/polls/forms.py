
from django import forms

from polls.models import ScaleChoice


class QuestionAnswerForm(forms.ModelForm):
    choice_score = forms.ChoiceField(
        choices=[
            (1, 'max_agree'),
            (2, 'med_agree'),
            (3, 'min_agree'),
            (4, 'neutral'),
            (5, 'min_disagree'),
            (6, 'med_disagree'),
            (7, 'max_disagree'),
        ],
        # required=True,
        widget=forms.RadioSelect(
            attrs={
                'class': 'form-control'
            }
        )
    )

    class Meta:
        model = ScaleChoice
        fields = ('choice_score',)

