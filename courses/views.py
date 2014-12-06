from django.shortcuts import get_object_or_404, render
from courses.models import Course


def courses_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/list.html', {'courses': courses})


def courses_item(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    return render(request, 'courses/item.html', {'course': course})
