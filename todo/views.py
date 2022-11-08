from django.shortcuts import render, redirect, get_object_or_404
from .models import Item
from .forms import ItemForm


# Create your views here.
def get_todo_list(request):
    items = Item.objects.all()
    context = {
        "items": items
    }
    return render(request, 'todo/todo_list.html', context)


# request param always for functions in views 
# add item
def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            Item.objects.create()

        return redirect('get_todo_list')
    # create an instance
    form = ItemForm()
    context = {
        'form': form
    }
    return render(request, 'todo/add_item.html', context)


# Edit Item
def edit_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)  # instance=item is the one we want to update  # noqa
        if form.is_valid():
            form.save()
            Item.objects.create()

        return redirect('get_todo_list')
    # create an instance, with this include the context
    # instance-Item is the pre-opopluated data
    form = ItemForm(instance=item)
    context = {
        'form': form
    }
    return render(request, 'todo/edit_item.html', context)


# Toggle Item
def toggle_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.done = not item.done
    item.save()
    return redirect('get_todo_list')


# Delete Item
def delete_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.delete()
    return redirect('get_todo_list')

