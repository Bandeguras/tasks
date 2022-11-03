from django.shortcuts import render
from webapp.models import Task
# Create your views here.


def index_view(request):
    tasks = Task.objects.order_by('-completion_at')
    context = {
        'tasks': tasks,
    }
    return render(request, 'index.html', context)
