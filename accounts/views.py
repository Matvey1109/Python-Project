from django.urls import reverse
from django.views.generic import TemplateView, ListView
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import redirect, render, HttpResponseRedirect
from django.contrib.auth.models import User

def accounts(request):
    return render(request, 'accounts/accounts.html')


class Sign_Up(TemplateView):
    template_name = "accounts/sign_up.html"

    def dispatch(self, request, *args, **kwargs):
        context = {}
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/main/')
            else:
                context['error'] = "Логин или пароль неверные"
        return render(request, self.template_name, context)


class Registration(TemplateView):
    template_name = "accounts/registration.html"

    def dispatch(self, request, *args, **kwargs):
        if request.method == 'POST':
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            password2 = request.POST.get('password2')

            if password == password2:
                User.objects.create_user(username, email, password)
                return redirect(reverse("sign_up"))

        return render(request, self.template_name)

class Logout(TemplateView):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/")