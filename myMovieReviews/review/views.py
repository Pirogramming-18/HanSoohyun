from django.shortcuts import render

# Create your views here.

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from .models import review

class ReviewListView(ListView):
    model = review

class ReviewCreateView(CreateView):
    model = review
    fields = ['title','year','genre','star', 'runningtime', 'reviewtext', 'director', 'actor' ]
    success_url = reverse_lazy('list')
    template_name_suffix = '_create'
class ReviewDetailView(DetailView):
    model = review
class ReviewUpdateView(UpdateView):
    model = review
    fields = ['title','year','genre','star', 'runningtime', 'reviewtext', 'director', 'actor' ]
    template_name_suffix = '_update'
class ReviewDeleteView(DeleteView):
    model = review
    success_url = reverse_lazy('list')