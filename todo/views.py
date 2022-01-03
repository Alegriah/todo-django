from django.shortcuts import render, redirect, get_object_or_404
from .forms import TodoForm
from .models import Todo
from django.utils import translation


def list_view(request):
    item_list = Todo.objects.order_by("-date")
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo')
    form = TodoForm()

    context = {
        "forms": form,
        "list": item_list,
        "title": "TODO LIST",
    }

    return render(request, "todo.html", context)


def delete_view(request, item_id):
    item = get_object_or_404(Todo, pk=item_id)
    item.delete()
    return redirect('todo',)


def detail_view(request, pk):
    todo = Todo.objects.get(pk=pk)
    context = {
        "todo": todo,
    }
    return render(request, "detail.html", context)


def category_view(request, category):
    item_list = Todo.objects.filter(
        category__name__contains=category
    )
    context = {
        "category": category,
        "list": item_list
    }
    return render(request, "category.html", context)
