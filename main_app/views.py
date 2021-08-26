from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Todo


def about(request):
  return render(request, 'about.html')

@login_required
def todos_index(request):
  todos = Todo.objects.filter(user=request.user)
  return render(request, 'todos/index.html', {'todos': todos})

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request,user)
      return redirect('todos_index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)

class TodoCreate(LoginRequiredMixin, CreateView):
  model = Todo
  fields = ['name', 'details', 'is_priority', 'is_completed']
  success_url = '/todos/'

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)


class TodoUpdate(LoginRequiredMixin, UpdateView):
  model = Todo
  fields = ['details', 'is_priority']
  success_url = '/todos/'

class TodoDelete(LoginRequiredMixin, DeleteView):
  model = Todo
  success_url = '/todos/'

  def get(self, request, *args, **kwargs):
    return self.post(request, *args, **kwargs)
  
class Home(LoginView):
  template_name = 'home.html'


