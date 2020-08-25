from django import forms
from .models import Recipe

class CreateRecipeForm(forms.ModelForm):
    # img =  forms.ImageField()
    class Meta:
        model = Recipe
        fields = ['title', 'description','image']

class UpdateRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'image']