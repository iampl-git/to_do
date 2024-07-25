from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo

def home(request):
    todos = Todo.objects.all()
    return render(request, 'index.html', {'todos': todos})

def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        status = request.POST.get('status')
        Todo.objects.create(name=name, description=description, status=status)
        return redirect('home')
    return render(request, 'create.html')

def edit(request):
    print("GET ID:", request.GET.get('id'))  # Debugging line
    if request.method == 'POST':
        id = request.POST.get('id')
        todo = get_object_or_404(Todo, id=id)
        
        todo.name = request.POST.get('name')
        todo.description = request.POST.get('description')
        todo.status = request.POST.get('status')
        todo.save()
        return redirect('home')
    
    id = request.GET.get('id')
    if not id:
        return redirect('home')
        
    todo = get_object_or_404(Todo, id=id)
    return render(request, 'edit.html', {'todo': todo})

