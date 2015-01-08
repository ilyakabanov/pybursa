from django.shortcuts import render
from django.shortcuts import get_object_or_404, render, redirect
from courses.models import Course
from django import forms

class CourseForm(forms.ModelForm):
	class Meta:
		model = Course


def courses_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/list.html', {'courses': courses})


def courses_item(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    return render(request, 'courses/item.html', {'course': course})


def courses_add(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            Course(**form.cleaned_data).save()
            return redirect('courses:index')
    else:
        form = CourseForm()

    return render(request, 'courses/add.html', {'form': form})


def courses_edit(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            for k, v in form.cleaned_data.items():
                setattr(course, k, v)
            course.save()
            return redirect('courses:detail', course.id)
    else:
        form = CourseForm({
            'lang': course.lang,
            'name': course.name,
            'slug': course.slug,
            'description': course.description,
            'coach': course.coach.id if course.coach else None,
            'assistant': course.assistant.id if course.assistant else None,
            'start_date': course.start_date,
            'end_date': course.end_date,
            'venue': course.venue.id if course.venue else None,
        })

    return render(request, 'courses/edit.html', {
        'form': form,
        'course': course,
    })


def courses_delete(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    course.delete()
    return redirect('courses:index')