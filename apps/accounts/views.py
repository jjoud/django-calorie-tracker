from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render

from apps.calories.forms import GoalForm
from apps.calories.models import Goal


def register(request):
    form = UserCreationForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        user = form.save()
        Goal.objects.create(user=user)
        login(request, user)
        return redirect('dashboard:dashboard')

    return render(request, 'accounts/register.html', {'form': form})


@login_required
def settings(request):
    goal, _created = Goal.objects.get_or_create(user=request.user)
    form = GoalForm(request.POST or None, instance=goal)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('dashboard:dashboard')

    return render(request, 'accounts/settings.html', {'form': form, 'goal': goal})
