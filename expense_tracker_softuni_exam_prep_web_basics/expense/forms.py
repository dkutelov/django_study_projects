from django import forms

from expense.models import Expense


class ExpenseForm(forms.ModelForm):
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


class DisabledFormMixin():
    def __init__(self, *args, **kwargs):
        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = True
            field.widget.attrs['readonly'] = True


class DeleteExpenseForm(ExpenseForm, DisabledFormMixin):
    def __init__(self, *args, **kwargs):
        ExpenseForm.__init__(self, *args, **kwargs)
        DisabledFormMixin.__init__(self)


