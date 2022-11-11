from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import Task
from webapp.forms import TaskForm
# Create your views here.


def index_view(request):
    tasks = Task.objects.order_by('-completion_at')
    context = {
        'tasks': tasks,
    }
    return render(request, 'index.html', context)


def task_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    context = {'task': task}
    return render(request, 'task_view.html', context)


def create_task_view(request):
    if request.method == 'GET':
        form = TaskForm()
        return render(request, "create_task.html", {'form': form})
    elif request.method == 'POST':
        form = TaskForm(data=request.POST)
        if form.is_valid():
            new_task = Task.objects.create(
                title=form.cleaned_data['title'],
                description=form.cleaned_data['description'],
                status=form.cleaned_data['status'],
                completion_at=form.cleaned_data['completion_at'],
            )
            return redirect('view', pk=new_task.pk)
        else:
            return render(request, "create_task.html", {'form': form})


def update_task_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'GET':
        form = TaskForm(initial={
            'title': task.title,
            'description': task.description,
            'status': task.status,
            'completion_at': task.completion_at,
        })
        return render(request, 'task_update.html', {'form': form})
    elif request.method == 'POST':
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task.title = form.cleaned_data.get('title')
            task.description = form.cleaned_data.get('description')
            task.status = form.cleaned_data.get('status')
            task.completion_at = form.cleaned_data.get('completion_at')
            task.save()
            return redirect('view', pk=task.pk)
        else:
            return render(request, 'task_update.html', {'form': form})


def delete_task_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'GET':
        return render(request, 'delete_task.html', {'task': task})
    elif request.method == 'POST':
        task.delete()
        return redirect('index')