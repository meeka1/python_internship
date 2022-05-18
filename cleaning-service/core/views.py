from re import template
from  .models.user  import User
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from  .forms  import  UserForm
from django.views.generic.list import ListView

class UserCreateView(CreateView):
    model = User
    template_name='create.html'
    fields="__all__"
    success_url='/'


class UserListView(ListView):
    model = User
    template_name="read.html" 


class UserDeleteView(DeleteView):
    template_name="delete.html"
    model = User
    success_url='/'


class UserUpdateView(UpdateView):
    model = User
    fields = '__all__'
    template_name='update.html'
    success_url='/'
    