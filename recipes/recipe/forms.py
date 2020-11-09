from django import forms

from django.core.validators import RegexValidator

from recipe.models import Recipe


class RecipeForm(forms.ModelForm):
    ingredients = forms.CharField(
        validators=[RegexValidator(r'(,\s)+',
                                   message='Ingredients should be words separated by comma and space')],
        widget=forms.TextInput()
    )

    class Meta:
        model = Recipe
        fields = '__all__'
        labels = {
            'image_url': 'Image URL',
            'time': 'Time (Minutes)'
        }


class DisabledFormMixin():
    def __init__(self):
        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = True
            field.widget.attrs['readonly'] = True


class DeleteRecipeForm(RecipeForm, DisabledFormMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        DisabledFormMixin.__init__(self)

