from django.contrib.auth.mixins import *
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render
from django.template.context_processors import request
from django.urls import *
from django.views.generic.edit import FormView
from django.contrib.auth import *
from .forms import *
from .models import *
from django.views.generic import *
from django.views.generic.detail import DetailView
from django.core.paginator import *

class RegisterUserView(FormView):
    template_name = "todo/register.html"
    form_class = RegisterUserForm
    success_url = 'todo/login.html'

    def form_valid(self, form):
        get_user_model().objects.create_user(form.cleaned_data.get('email'),
                                             form.cleaned_data.get('password'),
                                             form.cleaned_data.get('mobile_no'),
                                             form.cleaned_data.get('name')
                                             )

        return render(self.request, "todo/login.html")


class LoginUserView(FormView):
    template_name = "todo/login.html"
    form_class = LoginUserForm
    context_object_name = 'todo'

    def post(self, request, *args, **kwargs):
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'todo/index.html')

        else:
            return HttpResponse("invalid")


class LogoutView(FormView):
    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect('/')


class TodoDetailView(DetailView):
    model = Todo
    template_name = "todo/details.html"
    context_object_name = 'todos'


class TodoListView(LoginRequiredMixin, ListView):

    model = Todo
    template_name = "todo/list.html"
    paginate_by = 6

    def get_queryset(self):
        return Todo.objects.filter(creator=self.request.user)


class HomeView(TemplateView):
    template_name = 'todo/index.html'
    model = Todo

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        return context


class TodoUpdateView(LoginRequiredMixin, UpdateView):
    model = Todo
    form_class = TodoForm
    template_name = 'todo/update.html'
    success_url = '/'


class TodoAddView(LoginRequiredMixin, CreateView):
    model = Todo
    form_class = TodoForm
    template_name = 'todo/todo_form.html'

    success_url = reverse_lazy('list')

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super(TodoAddView, self).form_valid(form)


class TodoDeleteView(LoginRequiredMixin,DeleteView):
    model = Todo
    form_class = TodoForm
    template_name = 'todo/delete.html'
    success_url = reverse_lazy('list')

# @login_required
# def home(request):
#     return render(request, 'core/home.html')
