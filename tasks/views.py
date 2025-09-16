from django.shortcuts import get_object_or_404, render
from .models import Task


# Create your views here.
def task_list(request):
    tasks = Task.objects.all()
    print(request)
    return render(request, "tasks/task_list.html", {"tasks": tasks})


def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    print(request)
    return render(request, "tasks/task_detail.html", {"task": task})
