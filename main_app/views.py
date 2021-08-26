from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Todo


def home(request):
    return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def todos_index(request):
  todos = Todo.objects.all()
  return render(request, 'todos/index.html', {'todos': todos})


class TodoCreate(CreateView):
  model = Todo
  fields = '__all__'

class TodoUpdate(UpdateView):
  model = Todo
  fields = ['details', 'is_priority']
  success_url = '/todos/'

class TodoDelete(DeleteView):
  model = Todo
  success_url = '/todos/'

  def get(self, request, *args, **kwargs):
    return self.post(request, *args, **kwargs)


