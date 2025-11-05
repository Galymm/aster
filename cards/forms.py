from django import forms
from .models import Card, Category

class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ['question', 'answer', 'category']
        widgets = {
            'question': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите вопрос'}),
            'answer': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Введите ответ', 'rows': 3}),
            'category': forms.Select(attrs={'class': 'form-select'}),
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'parent']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Например: Python'}),
            'parent': forms.Select(attrs={'class': 'form-select'}),
        }
