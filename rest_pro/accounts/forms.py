from django import forms
from .models import Expense


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['category', 'price', 'description', 'user']
        widgets = {
            'user': forms.HiddenInput(),
            'category': forms.TextInput(attrs={
                'placeholder': 'Category',
                'class': 'form-control'
            }),
            'price': forms.TextInput(attrs={
                'placeholder': 'Price',
                'class': 'form-control'
            }),
            'description': forms.TextInput(attrs={
                'placeholder': 'Description',
                'class': 'form-control'
            })
        }
