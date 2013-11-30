from django.shortcuts import render

from django.views.generic.detail import DetailView
from partz.models import Project, Media, Note

# Create your views here.

class ProjectDetailView(DetailView):
  model = Project
  
  def get_context_data(self, **kwargs):
    context = super(ProjectDetailView, self).get_context_data(**kwargs)
    context['greeting'] = "Hello!"
    return context

