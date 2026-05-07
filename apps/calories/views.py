from collections import defaultdict

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.utils import timezone

from .forms import FoodForm, MealForm
from .models import Food, Goal, Meal


def get_goal_for_user(user):
    goal, _created = Goal.objects.get_or_create(user=user)
    return goal


@login_required
def add_meal(request):
    form = MealForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        meal = form.save(commit=False)
        meal.user = request.user
        meal.save()
        return redirect('dashboard:dashboard')

    return render(request, 'calories/add_meal.html', {'form': form})


@login_required
def food_list(request):
    foods = Food.objects.all()
    form = FoodForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('calories:food_list')

    return render(request, 'calories/food_list.html', {'foods': foods, 'form': form})


@login_required
def history(request):
    meals = Meal.objects.filter(user=request.user).select_related('food')
    totals = defaultdict(int)

    for meal in meals:
        meal_date = timezone.localtime(meal.eaten_at).date()
        totals[meal_date] += meal.total_calories

    history_totals = [
        {'date': date, 'total': total}
        for date, total in sorted(totals.items(), reverse=True)
    ]

    return render(
        request,
        'calories/history.html',
        {'meals': meals, 'history_totals': history_totals},
    )
