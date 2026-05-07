from django import forms

from .models import Food, Goal, Meal


class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ['name', 'calories', 'serving_size']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Chicken salad'}),
            'calories': forms.NumberInput(attrs={'placeholder': '420', 'min': 1}),
            'serving_size': forms.TextInput(attrs={'placeholder': '1 bowl'}),
        }


class MealForm(forms.ModelForm):
    class Meta:
        model = Meal
        fields = ['food', 'servings', 'eaten_at', 'notes']
        widgets = {
            'servings': forms.NumberInput(attrs={'step': '0.25', 'min': '0.25'}),
            'eaten_at': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'notes': forms.TextInput(attrs={'placeholder': 'Optional note'}),
        }


class GoalForm(forms.ModelForm):
    class Meta:
        model = Goal
        fields = ['daily_calorie_goal']
        labels = {'daily_calorie_goal': 'Daily calorie goal'}
        widgets = {
            'daily_calorie_goal': forms.NumberInput(attrs={'min': 1, 'placeholder': '2000'}),
        }
