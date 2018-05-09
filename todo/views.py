from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.edit import FormView
from django.contrib.auth import *
from .forms import *
from .models import *
from django.views.generic import *
from django.views.generic.detail import DetailView



def index(request):
    todos = Todo.objects.all()
    form = TodoForm()
    context = {'todos': todos, 'form': form}
    return render(request, 'todo/index.html', context)


def add_todo(request):
    form = TodoForm()
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save()
            return HttpResponseRedirect('/')
    return render(request, 'todo/todo_form.html', {'form': form})


def delete_all(request):
    Todo.objects.all().delete()
    return redirect('index')


def check_todo(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.checked = True
    todo.save()
    return redirect('index')


def uncheck_todo(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.checked = False
    todo.save()
    return redirect('index')


def delete_completed(request):
    Todo.objects.filter(checked=True).delete()
    return redirect('index')


class RegisterUserView(FormView):
    template_name = "todo/register.html"
    form_class = RegisterUserForm
    success_url = 'todo/home/'

    def form_valid(self, form):
        get_user_model().objects.create_user(form.cleaned_data.get('email'),
                                                 form.cleaned_data.get('password'),
                                                 form.cleaned_data.get('mobile_no'),
                                                 form.cleaned_data.get('name')
                                                 )

        return render(self.request, "todo/index.html")


class LoginUserView(FormView):
    template_name = "todo/login.html"
    form_class = LoginUserForm

    def post(self, request, *args, **kwargs):
        email = request.POST['email']
        password = request.POST['password']
        # try:
        print(email, password, "dddddddddddddd")
        user = authenticate(request, email=email, password=password)
        print("auth", str(authenticate(email=email, password=password)))

        if user is not None:
            login(request, user)
            return render(request, 'todo/index.html')

        else:
            return HttpResponse("invalid")



class TodoDetail(DetailView):
        model = Todo
        template_name = "todo/details.html"
        context_object_name = 'todos'


class TodoList (ListView):
        model = Todo
        template_name = "todo/list.html"
        context_object_name = 'todo'

class HomeView(TemplateView):

    template_name = 'todo/index.html'
