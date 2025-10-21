from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as loginUser, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from app.forms import TODOForm
from app.models import TODO
from django.utils import timezone
from django.db.models import Q

@login_required(login_url='login')
def home(request):
    user = request.user
    form = TODOForm()
    # Filtering & search (use GET params)
    q = request.GET.get('q', '')  # search query
    category = request.GET.get('category', '')
    status = request.GET.get('status', '')
    order = request.GET.get('order', 'priority')  # ordering field

    todos = TODO.objects.filter(user=user)

    if q:
        todos = todos.filter(Q(title__icontains=q) | Q(description__icontains=q))
    if category:
        todos = todos.filter(category=category)
    if status:
        todos = todos.filter(status=status)

    if order == 'date':
        todos = todos.order_by('-date')
    elif order == 'due':
        todos = todos.order_by('due_date')
    else:
        todos = todos.order_by('priority')

    # progress: percent completed
    total = todos.count()
    completed = todos.filter(status='C').count()
    progress = int((completed / total) * 100) if total > 0 else 0

    context = {
        'form': form,
        'todos': todos,
        'q': q,
        'category': category,
        'status': status,
        'order': order,
        'progress': progress,
        'total': total,
        'completed': completed,
    }
    return render(request, 'index.html', context=context)

def login(request):
    if request.method == 'GET':
        form = AuthenticationForm()
        context = {"form": form}
        return render(request, 'login.html', context=context)
    else:
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                loginUser(request, user)
                return redirect('home')
        context = {"form": form}
        return render(request, 'login.html', context=context)

def signup(request):
    if request.method == 'GET':
        form = UserCreationForm()
        context = {"form": form}
        return render(request, 'signup.html', context=context)
    else:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user is not None:
                return redirect('login')
        context = {"form": form}
        return render(request, 'signup.html', context=context)

@login_required(login_url='login')
def add_todo(request):
    user = request.user
    if request.method == 'POST':
        form = TODOForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = user
            # if status is completed, set completed_at
            if todo.status == 'C' and not todo.completed_at:
                todo.completed_at = timezone.now()
            todo.save()
            return redirect("home")
        else:
            # re-render with validation errors
            todos = TODO.objects.filter(user=user).order_by('priority')
            return render(request, 'index.html', context={'form': form, 'todos': todos})
    return redirect('home')

@login_required(login_url='login')
def edit_todo(request, id):
    user = request.user
    todo = get_object_or_404(TODO, pk=id, user=user)
    if request.method == 'GET':
        form = TODOForm(instance=todo)
        return render(request, 'edit_todo.html', context={'form': form, 'todo': todo})
    else:
        form = TODOForm(request.POST, instance=todo)
        if form.is_valid():
            todo = form.save(commit=False)
            # update completed_at logically
            if todo.status == 'C' and not todo.completed_at:
                todo.completed_at = timezone.now()
            if todo.status == 'P':
                todo.completed_at = None
            todo.save()
            return redirect('home')
        return render(request, 'edit_todo.html', context={'form': form, 'todo': todo})

@login_required(login_url='login')
def delete_todo(request, id):
    todo = get_object_or_404(TODO, pk=id, user=request.user)
    todo.delete()
    return redirect('home')

@login_required(login_url='login')
def change_todo(request, id, status):
    todo = get_object_or_404(TODO, pk=id, user=request.user)
    todo.status = status
    if status == 'C':
        todo.completed_at = timezone.now()
    else:
        todo.completed_at = None
    todo.save()
    return redirect('home')

def signout(request):
    logout(request)
    return redirect('login')
