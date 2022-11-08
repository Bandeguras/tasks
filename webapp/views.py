from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import Task, STATUS_CHOICES
# Create your views here.


def index_view(request):
    if request.method == 'POST':
        task_id = request.GET.get('id')
        task = Task.objects.get(id=task_id)
        task.delete()
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
        return render(request, "create_task.html", {'statuses': STATUS_CHOICES})
    elif request.method == 'POST':
        description = request.POST.get('description')
        status = request.POST.get('status')
        completion_at = request.POST.get('completion_at')
        if completion_at == '':
            completion_at = None
        new_task = Task.objects.create(description=description, status=status, completion_at=completion_at)
        return redirect('view', pk=new_task.pk)