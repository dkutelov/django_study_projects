from django import forms

from expense.models import Expense


class ExpenseForm(forms.ModelForm):
    # title = forms.CharField(label='Title', max_length=50)
    # image_url = forms.URLField(label='Link to Image', max_length=200)
    # description = forms.CharField(
    #     label='Description',
    #     widget=forms.Textarea
    # )
    # price = forms.FloatField(
    #     label='Price',
    #     min_value=0
    # )

    class Meta:
        model = Expense
        fields = ['title', 'description', 'image_url', 'price']
        labels = {
            'title': 'Title',
            'image_url': 'Link to Image',
            'description': 'Description',
            'price': 'Price'
        }
        widgets = {
            'description': forms.Textarea()
        }
