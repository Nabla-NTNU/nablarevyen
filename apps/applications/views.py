from django.shortcuts import render
from django.utils import timezone
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic import CreateView, TemplateView
from django.views.generic.edit import FormMixin

from ..groups.models import Group
from .models import Position
from .forms import ApplicationForm


class ApplicationView(CreateView):

    form_class = ApplicationForm
    template_name = 'applications/form.html'
    success_url = reverse_lazy('applications:success')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        group_list = Group.objects.filter(published=True)
        open_positions = Position.objects.filter(published=True, deadline__gte=timezone.now(), open__lte=timezone.now()).count()
        context['group_list'] = group_list
        context['open_positions'] = open_positions
        return context


class ApplicationSuccessView(TemplateView):

    template_name = 'applications/form_success.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        group_list = Group.objects.filter(published=True)
        context['group_list'] = group_list
        return context
