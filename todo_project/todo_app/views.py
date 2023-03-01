from django.shortcuts import render, redirect
from .forms import todo_forms
from todo_app.models import Task
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy


# views using class
class TaskListView(ListView):
    model = Task
    template_name = 'home.html'
    context_object_name = 'obj'


class TaskDetailView(DetailView):
    model = Task
    template_name = 'dview.html'
    context_object_name = 'i'


class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'edit.html'
    context_object_name = 'task1'
    fields = ('name', 'priority', 'date')

    def get_success_url(self):
        return reverse_lazy('cbvdetail', kwargs={'pk': self.object.id})


class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvlist')


# Create your views here.Using functions
def home(request):
    obj1 = Task.objects.all()
    if request.method == 'POST':
        name = request.POST['name']
        priority = request.POST['priority']
        date = request.POST['date']
        obj = Task(name=name, priority=priority, date=date)
        obj.save()
        obj1 = Task.objects.all()

    return render(request, 'home.html', {'obj': obj1})


def delete(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('/')
    return render(request, 'delete.html')


def update(request, task_id):
    task = Task.objects.get(id=task_id)
    forms = todo_forms(request.POST or None, instance=task)
    if forms.is_valid():
        forms.save()
        return redirect('/')
    return render(request, 'update.html', {'tasks': task, 'forms': forms})
