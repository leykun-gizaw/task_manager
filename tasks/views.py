from django.shortcuts import get_object_or_404, render, redirect
from .models import Task
from .forms import CustomUserCreationForm, TaskForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def task_list(request):
    tasks = Task.objects.all()
    print(request)
    return render(request, "tasks/task_list.html", {"tasks": tasks})


@login_required
def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    print(request)
    return render(request, "tasks/task_detail.html", {"task": task})


@login_required
def task_create(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.created_by = request.user
            task.save()
            return redirect("tasks:task_list")
        pass
    else:
        form = TaskForm()
        pass
    return render(request, "tasks/task_form.html", {"form": form})


@login_required
def task_update(request, pk):
    task = Task.objects.get(pk=pk)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("tasks:task_list")
    else:
        form = TaskForm(instance=task)
    return render(request, "tasks/task_form.html", {"form": form})


@login_required
def task_delete(request, pk):
    task = Task.objects.get(pk=pk)
    # if the method is post delete the task if not redirect to tasks list
    if request.method == "POST":
        task.delete()
        return redirect("tasks:task_list")
    return render(request, "tasks/task_confirm_delete.html", {"task": task})


def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = CustomUserCreationForm()
    return render(request, "registration/register.html", {"form": form})
