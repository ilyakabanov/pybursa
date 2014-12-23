from django.shortcuts import get_object_or_404, render, redirect

from students.models import Student
from students.forms import StudentForm


def students_list(request):
    students = Student.objects.all()
    return render(request, 'students/list.html', {'students': students})


def students_item(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    return render(request, 'students/item.html', {'student': student})


def students_add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            Student(**form.cleaned_data).save()
            return redirect('students:index')
    else:
        form = StudentForm()

    return render(request, 'students/add.html', {'form': form})


def students_edit(request, student_id):
    student = get_object_or_404(Student, id=student_id)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            student.save()
            return redirect('students:detail', student.id)
    else:
        form = StudentForm(instance=student)

    return render(request, 'students/edit.html', {
        'form': form,
        'student': student
    })


def students_delete(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    student.delete()
    return redirect('students:index')
