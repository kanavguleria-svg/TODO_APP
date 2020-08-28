from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages

from .forms import Todo_App_Form
from .models import Todo


def index(request):
    list = Todo.objects.order_by("-date")
    if request.method == "POST":
        form = Todo_App_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo')
    form = Todo_App_Form()

    todo_dict = { "forms" : form, "list" : list, "title" : "TODO LIST",}

    return render(request, 'todo_app/index.html', todo_dict)


def remove(request,item_id):
    item = Todo.objects.get(id=item_id)
    item.delete()
    messages.info(request, "task removed") 
    return redirect('todo')
