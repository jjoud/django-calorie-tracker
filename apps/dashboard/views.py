from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils import timezone

from apps.calories.models import Goal, Meal


def landing(request):
    if request.user.is_authenticated:
        return dashboard(request)
    return render(request, 'dashboard/landing.html')


@login_required
def dashboard(request):
    today = timezone.localdate()
    goal, _created = Goal.objects.get_or_create(user=request.user)
    today_meals = Meal.objects.filter(
        user=request.user,
        eaten_at__date=today,
    ).select_related('food')

    total_calories = sum(meal.total_calories for meal in today_meals)
    remaining_calories = max(goal.daily_calorie_goal - total_calories, 0)
    progress_percentage = min(
        round((total_calories / goal.daily_calorie_goal) * 100),
        100,
    )

    context = {
        'goal': goal,
        'today_meals': today_meals,
        'total_calories': total_calories,
        'remaining_calories': remaining_calories,
        'progress_percentage': progress_percentage,
    }
    return render(request, 'dashboard/dashboard.html', context)
