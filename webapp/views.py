from django.shortcuts import render
from webapp.models import Task, STATUS_CHOICES
# Create your views here.


def index_view(request):
    tasks = Task.objects.order_by('-completion_at')
    context = {
        'tasks': tasks,
    }
    return render(request, 'index.html', context)

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
        context = {'task': new_task}
        return render(request, 'task_view.html', context)