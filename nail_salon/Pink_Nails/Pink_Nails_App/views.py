from django.shortcuts import render
# Create your views here.
from django.views.generic import (TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView)


class IndexTemplateView(TemplateView):
    template_name = 'index.html'

class ServicesTemplateView(TemplateView):
    template_name = 'services.html'

class ContactTemplateView(TemplateView):
    template_name = 'contact.html'
