from datetime import datetime
from random import random

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.shortcuts import redirect, render
from django.template import loader
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView

from student.forms import StudentForm, StudentUpdateForm
from student.models import Student, HistoryStudent
from userextend.models import History


# CreateView -> folosit pentru a genera un formular pe baza modelului si pentru a salva datele in baza de date
# SuccessMessageMixin - folosit pentru a afisa un mesaj de success in momentul in care actiunea a fost realizata
# cu success
# PermissionReuiredMixin -> verificam daca userul logat are permisiunea respectiva, daca user logat NU ARE permisiunea
# respectiva va fi redirectionat catre pagina 403 (HTTP STATUS)

def student(request):
    context = {
        # Your context data here
    }
    html_template = loader.get_template("student/student.html")
    # return HttpResponse(html_template.render(context, request))

    return render(request, 'student/student.html', context)
class StudentCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'student/create_student.html'
    model = Student
    form_class = StudentForm
    success_url = reverse_lazy('list-of-students')
    success_message = '{f_name} {l_name}'

    def get_success_message(self, cleaned_data):
        if self.object.gender == 'male':
            message = self.success_message + ' ' + 'a fost adaugat cu succes'
        else:
            message = self.success_message + ' ' + 'a fost adaugata cu succes'

        return message.format(f_name=self.object.first_name, l_name=self.object.last_name)

    def form_valid(self, form):
        if form.is_valid():
            new_student = form.save(commit=False)
            new_student.first_name = new_student.first_name.title()
            new_student.last_name = new_student.last_name.title()
            new_student.save()

            # History
            get_message = (f'Studentul cu numele {new_student.first_name} {new_student.last_name}'
                           f' a fost adaugat de catre {self.request.user.username}.')

            HistoryStudent.objects.create(message=get_message, created_at=datetime.now(), active=True,
                                          user_id=self.request.user.id)

        return redirect('login')


#listaView - il folosim pentru a afisa inregistrarile din tabela student_student

class StudentListView(LoginRequiredMixin, ListView):
    template_name = 'student/list_of_student.html'
    model = Student
    context_object_name = 'all_students'  #Student.object.all()

    def get_queryset(self):
        return Student.objects.filter(active=True)


# UpdateView -> il folosimt pentru a actualiza datele unui student
class StudentUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'student/update_student.html'
    model = Student
    form_class = StudentUpdateForm
    success_url = reverse_lazy('list-of-students')


class StudentDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'student/delete_student.html'
    model = Student
    success_url = reverse_lazy('list-of-students')


class StudentDetailView(LoginRequiredMixin, DetailView):
    template_name = 'student/details_student.html'
    model = Student

@login_required()
def search(request):
    get_value = request.GET.get('filter')
    if get_value:
        students = Student.objects.filter(Q(last_name__icontains=get_value) | Q(first_name__icontains=get_value))
    else:
        students = Student.objects.all()

    return render(request, 'student/list_of_student.html', {'all_students': students})
