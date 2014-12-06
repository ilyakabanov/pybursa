from django.shortcuts import get_object_or_404, render
from coaches.models import Coach


def coaches_list(request):
    coaches = Coach.objects.all()
    return render(request, 'coaches/list.html', {'coaches': coaches})


def coaches_item(request, coach_id):
    coach = get_object_or_404(Coach, id=coach_id)
    return render(request, 'coaches/item.html', {'coach': coach})
