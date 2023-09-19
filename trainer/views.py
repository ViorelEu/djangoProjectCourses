from datetime import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.template import loader
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView

from trainer.forms import TrainerForm
from trainer.models import Trainer

def trainer(request):
    context = {
        # Your context data here
    }
    html_template = loader.get_template("trainer/trainers.html")
    # return HttpResponse(html_template.render(context, request))

    return render(request, 'trainer/trainers.html', context)
class TrainerCreateView(CreateView):
    template_name = 'trainer/trainer_page.html'
    model = Trainer
    form_class = TrainerForm
    success_url = reverse_lazy('index')


class TrainerListView(ListView):
    template_name = 'trainer/list_of_trainer.html'
    model = Trainer
    context_object_name = 'all_trainers'

    def get_queryset(self):
        return Trainer.objects.filter(active=True)


class TrainerUpdateView(UpdateView):
    template_name = 'trainer/update_trainer.html'
    model = Trainer
    form_class = TrainerForm
    success_url = reverse_lazy('list-of-trainers')


class TrainerDeleteView(DeleteView):
    template_name = 'trainer/delete_trainer.html'
    model = Trainer
    success_url = reverse_lazy('list-of-trainers')


class TrainerDetailView(DetailView):
    template_name = 'trainer/detail_trainer.html'
    model = Trainer
