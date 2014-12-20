from django.shortcuts import get_object_or_404, render, redirect

from coaches.models import Coach
from coaches.forms import CoachForm


def coaches_list(request):
    coaches = Coach.objects.all()
    return render(request, 'coaches/list.html', {'coaches': coaches})


def coaches_item(request, coach_id):
    coach = get_object_or_404(Coach, id=coach_id)
    return render(request, 'coaches/item.html', {'coach': coach})


def coaches_add(request):
    if request.method == 'POST':
        form = CoachForm(request.POST)
        if form.is_valid():
            Coach(**form.cleaned_data).save()
            return redirect('coaches:index')
    else:
        form = CoachForm()

    return render(request, 'coaches/add.html', {'form': form})


def coaches_edit(request, coach_id):
    coach = get_object_or_404(Coach, id=coach_id)

    if request.method == 'POST':
        form = CoachForm(request.POST, instance=coach)
        if form.is_valid():
            coach.save()
            return redirect('coaches:detail', coach.id)
    else:
        form = CoachForm(instance=coach)

    return render(request, 'coaches/edit.html', {'form': form, 'coach': coach})


def coaches_delete(request, coach_id):
    coach = get_object_or_404(Coach, id=coach_id)
    coach.delete()
    return redirect('coaches:index')
