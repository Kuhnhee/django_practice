from django.shortcuts import render, redirect, get_object_or_404

from .models import Todo

# Create your views here.
def index(request):
    todos = Todo.objects.all()
    context = {
        'todos' : todos,
    }

    return render(request, 'todos/index.html', context)

# def new(request):
#     return render(request, 'todos/new.html')

# new와 create를 합침
def create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        due_date = request.POST.get('due-date')

        Todo.objects.create(title=title, due_date=due_date)

        return redirect('todos:index')
    else:   # GET일 때
        return render(request, 'todos/create.html')

# def edit(request, pk):
#     todo = Todo.objects.get(pk=pk)
#     context = {
#         'todo':todo,
#     }
#     return render(request, 'todos/edit.html', context)

# edit과 update를 합침
def update(request, pk):
    todo = get_object_or_404(Todo, id=pk) #object가 있으면 나오고, 없으면 404 에러
    # todo = Todo.objects.get(pk=pk)
    if request.method == 'POST':
        title = request.POST.get('title')
        due_date = request.POST.get('due-date')
        
        todo.title = title
        todo.due_date = due_date
        todo.save()

        return redirect('todos:index')
    else: # GET 때
        context = {
            'todo':todo,
        }
        return render(request, 'todos/update.html', context)


def delete(request, pk):
    todo = get_object_or_404(Todo, id=pk)
    # todo = Todo.objects.get(id=pk)
    todo.delete()
    
    return redirect('todos:index')