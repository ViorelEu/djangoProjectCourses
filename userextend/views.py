from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.models import User
from userextend.forms import UserForm
from userextend.models import History
from django.core.mail import send_mail
from django.template.loader import get_template
from django.core.mail import EmailMessage
from djangoProjectCourses.settings import EMAIL_HOST_USER
import random

class UserCreateView(CreateView):
    template_name = 'userextend/create_user.html'
    model = User
    form_class = UserForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.first_name = new_user.first_name.title()
            new_user.last_name = new_user.last_name.title()
            new_user.username = f'{new_user.first_name[0].lower()}{new_user.last_name.lower().replace(" ", "")}_{random.randint(100000, 999999)}'
            new_user.save()

            get_message = (f'Userul a fost adaugat cu success. Username: {new_user.username}, email:{new_user.email}, '
                           f'first_name: {new_user.first_name}, last_name:{new_user.last_name}')
            History.objects.create(message=get_message, created_at=datetime.now(), active=True)

            subject = 'Adding a new account'
            message = f'Congratulations! Your username is: {new_user.username}.'


            details_user = {
                'fullname': f'{new_user.first_name} {new_user.last_name}',
                'username': new_user.username
            }

            subject = 'Adding a new account'
            message = get_template('mail.html').render(details_user)

            mail = EmailMessage(
                subject,
                message,
                EMAIL_HOST_USER,
                [new_user.email]
            )
            mail.content_subtype = 'html'
            mail.send()

            return redirect('login')


class UserProfile(DetailView):
    model = User
    template_name = 'userextend/userp_profile.html'


