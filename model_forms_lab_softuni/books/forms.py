from django import forms
from django.core.exceptions import ValidationError

from books.models import Book


class BookForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_form_control_class_to_all()

    def add_form_control_class_to_all(self):
        for (_, field) in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    def clean_pages(self):
        page = self.cleaned_data['pages']
        if page <= 0:
            raise ValidationError(f'Pages should be more than zero!')
        return page

    class Meta:
        model = Book
        fields = '__all__'
        # exlcude - to remove some fields
        # widgets = {
        #     'title': forms.TextInput(
        #         attrs={
        #             'class': 'form-control'
        #         }
        #     ),
        #     'description': forms.TextInput(
        #         attrs={
        #             'class': 'form-control'
        #         }
        #     ),
        #     'pages': forms.NumberInput(
        #         attrs={
        #             'class': 'form-control'
        #         }
        #     ),
        #     'author': forms.TextInput(
        #         attrs={
        #             'class': 'form-control'
        #         }
        #     ),
        # }
