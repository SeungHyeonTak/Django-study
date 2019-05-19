from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from .models import Bookmake
from django.views.generic.edit import UpdateView,DeleteView,CreateView

class BookmakeList(ListView):
    model = Bookmake
    template_name_suffix = '_list'

class BookmakeUpdate(UpdateView):
    model = Bookmake
    template_name_suffix = '_update'
    fields = ['site_name', 'url']
    success_url = '/'

class BookmakeDelte(DeleteView):
    model = Bookmake
    template_name_suffix = '_delete'
    fields = ['site_name', 'url']