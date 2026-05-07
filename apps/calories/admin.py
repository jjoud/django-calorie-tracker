from django.contrib import admin

from .models import Food, Goal, Meal


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'calories', 'serving_size')
    search_fields = ('name',)


@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    list_display = ('user', 'food', 'servings', 'eaten_at')
    list_filter = ('eaten_at',)
    search_fields = ('user__username', 'food__name')


@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    list_display = ('user', 'daily_calorie_goal', 'updated_at')

# Register your models here.
