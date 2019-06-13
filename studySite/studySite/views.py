from django.shortcuts import render, get_object_or_404
from django.views import generic
from account.models import User

class index(generic.TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Hello Home page'
        return context