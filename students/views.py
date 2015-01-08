from django.shortcuts import render, redirect, get_object_or_404
from students.models import Student
from django import forms
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView, CreateView, UpdateView


class StudentListView(ListView):
    template_name = "students/list.html"
    model = Student
    #queryset = Student.objects.filter(package='vip')
    context_object_name = "students"

    def get_queryset(self):
        filter_package = self.request.GET.get('package')
        return Student.objects.filter(package=filter_package)


def students_list(request):
    students = Student.objects.all()
    page_title = 'students list'
    return render(request, 'students/list.html', 
                         {'students': students,
                          'title': page_title})


class StudentView(DetailView):
    template_name = "students/item.html"
    model = Student
    context_object_name = "student"


class StudentForm(forms.Form):
    PACKAGE_CHOICES = (
        ('standart', 'Standart'),
        ('gold', 'Gold'),
        ('vip', 'VIP'),
        )
    student_name = forms.CharField(max_length=100)
    student_package = forms.ChoiceField(choices=PACKAGE_CHOICES, widget=forms.RadioSelect)
    #student_note = forms.CharField(widget=forms.Textarea)


# def student_edit(request, student_id):
#     student = Student.objects.get(id=student_id)
#     if request.method == 'POST':
#         form = StudentForm(request.POST)
#         if form.is_valid():
#             student.name = form.cleaned_data['student_name']
#             student.package = form.cleaned_data['student_package']
#             student.save()
#             return redirect('student-edit', student.id)
#     else:
#         form = StudentForm(initial={'student_name': student.name, 
#                                     'student_package': student.package})
#     return render(request, 'students/edit.html', {'form': form})



class StudentModelForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'package']
        widgets = {
            'package': forms.RadioSelect
            }

class StudentCreateView(CreateView):
    template_name = "students/edit.html"
    form_class = StudentModelForm
    model = Student

    def get_context_data(self, **kwargs):
        context = super(StudentCreateView, self).get_context_data(**kwargs)
        context['title'] = "Student create item"
        return context


class StudentUpdateView(UpdateView):
    template_name = "students/edit.html"
    form_class = StudentModelForm
    model = Student

    def get_context_data(self, **kwargs):
        context = super(StudentUpdateView, self).get_context_data(**kwargs)
        context['title'] = "Student edit item"
        return context


def student_edit(request, student_id):
    title = "Student edit item"
    student = Student.objects.get(id=student_id)
    if request.method == 'POST':
        form = StudentModelForm(request.POST, instance=student)
        if form.is_valid():
            student = form.save()
            return redirect('student-edit', student.id)
    else:
        form = StudentModelForm(instance=student)
    return render(request, 'students/edit.html', {'form': form, 'title': title})


def student_add(request):
    title = "Student add item"
    if request.method == 'POST':
        form = StudentModelForm(request.POST)
        if form.is_valid():
            student = form.save()
            return redirect('student-edit', student.id)
    else:
        form = StudentModelForm()
    return render(request, 'students/edit.html', {'form': form, 'title': title})


def student_add_edit(request, student_id=None):
    student = None
    if student_id is not None:
        student = get_object_or_404(Student, id=student_id)
    
    if request.method == 'POST':
        form = StudentModelForm(request.POST, instance=student)
        if form.is_valid():
            student = form.save()
            return redirect('student-edit', student.id)
    else:
        form = StudentModelForm(instance=student)
    return render(request, 'students/edit.html', {'form': form})



