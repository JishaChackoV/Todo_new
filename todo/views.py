from django.contrib.auth.hashers import make_password
from django.contrib.auth.mixins import *
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import *
from django.contrib.auth import *
from .forms import *
from .models import *
from django.views.generic import *
from django.views.generic.detail import DetailView
from django.core.mail import send_mail
from django.core.signing import Signer
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string


class RegisterUserView(FormView):
    Model = UserProfile
    template_name = "todo/register.html"
    form_class = RegisterUserForm
    success_url = '/login'

    def form_valid(self, form):
        # get_user_model().objects.create_user(form.cleaned_data.get('username'),
        #                                      form.cleaned_data.get('password'),
        #                                      form.cleaned_data.get('mobile_no'),
        #                                      form.cleaned_data.get('email')
        #                                      )
        obj = form.save(commit=False)
        obj.password = make_password(obj.password)
        #obj.is_active = False
        signer = Signer()
        signed_value = signer.sign(obj.email)
        key = ''.join(signed_value.split(':')[1:])
        reg_obj = Registration.objects.create(user=obj, key=key)
        msg_html = render_to_string('todo/acc_active_email.html', {'key': key})
        send_mail("123", "123", 'anjitha.test@gmail.com', [obj.email], html_message=msg_html, fail_silently=False)
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):

        form = RegisterUserForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            email = request.POST.get('email')
            mobile_no = request.POST.get('mobile_no')
            password = request.POST.get('password')
            UserProfile.objects.create_user(username, password, mobile_no, email)
            return HttpResponseRedirect('/login')
        else:
            return render(request, "todo/register.html", {'form': form})
        return re


class LoginUserView(FormView):
    template_name = "todo/login.html"
    form_class = LoginUserForm
    context_object_name = 'todo'

    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

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


class AduserListView(LoginRequiredMixin, ListView):
    model = Todo
    template_name = "todo/adminlist.html"
    paginate_by = 6
    success_url = reverse_lazy('/')

    def get_queryset(self):
        return Todo.objects.all()


class RegistrationSuccess(TemplateView):
    template_name = 'todo/registrationsuccess.html'

    def get(self, request, args, *kwargs):
        key = self.kwargs.get("key")
        try:
            reg_obj = Registration.objects.get(key=key)
            obj = RegisterUserView.objects.get(id=reg_obj.user_id)
            obj.is_active = True
            obj.save()
            context = {'user': reg_obj, 'status': True}
            return self.render_to_response(context)
        except Registration.DoesNotExist:
            return self.render_to_response({'status': False})
