from django import forms
from .models import Expense

class ExpenseForm(forms.Form):
    class Meta:
        model = Expense
        fields = ['category','price','description','user']
        widgets = {
            'category' : forms.CharField(attrs={
                'placeholder':'Category',
                'class':'form-control'
            }),
            'price': forms.CharField(attrs={
                'placeholder': 'Price',
                'class':'form-control'
            }),
            'Description':forms.CharField(attrs={
                'placeholder': 'Description',
                'class': 'form-control'
            })
        }
        
