from re import template
from  .models  import Film
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from  .forms  import  FilmForm
from django.views.generic.list import ListView

class FilmCreateView(CreateView):
    model = Film
    template_name='create.html'
    fields="__all__"
    success_url='/'


class FilmListView(ListView):
    model = Film
    template_name="read.html" 


class FilmDeleteView(DeleteView):
    template_name="delete.html"
    model = Film
    success_url='/'


class FilmUpdateView(UpdateView):
    model = Film
    fields = '__all__'
    template_name='update.html'
    success_url='/'
    