from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Food(models.Model):
    name = models.CharField(max_length=120)
    calories = models.PositiveIntegerField(help_text='Calories per serving')
    serving_size = models.CharField(max_length=80, default='1 serving')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'{self.name} ({self.calories} cal)'


class Meal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='meals')
    food = models.ForeignKey(Food, on_delete=models.CASCADE, related_name='meals')
    servings = models.DecimalField(max_digits=5, decimal_places=2, default=1)
    eaten_at = models.DateTimeField(default=timezone.now)
    notes = models.CharField(max_length=255, blank=True)

    class Meta:
        ordering = ['-eaten_at']

    @property
    def total_calories(self):
        return round(float(self.food.calories) * float(self.servings))

    def __str__(self):
        return f'{self.food.name} - {self.total_calories} cal'


class Goal(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='goal')
    daily_calorie_goal = models.PositiveIntegerField(default=2000)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username}: {self.daily_calorie_goal} cal/day'
