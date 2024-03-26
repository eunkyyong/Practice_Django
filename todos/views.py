from django.shortcuts import render
from .models import Todo

# Create your views here.
def index(request):
    # work = request.GET.get('work')
    # context = {
    #     'work': work
    # }
    # ORM: 객체지향언어를 이용해서 DB에 접근해서 가져와! -> QuerySet api
    todos = Todo.objects.all()
    context = {
        'todos' : todos  # todos/index.html이랑 합칠 때 그 이름
    }
    return render(request, 'todos/index.html', context)

def create_todo(request):
    return render(request, 'todos/create_todo.html')

def detail(request, todo_pk):
    todo = Todo.objects.get(pk=todo_pk)
    context = {
        'todo': todo
    }
    return render(request, 'todos/detail.html', context)