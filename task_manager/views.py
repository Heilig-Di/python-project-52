from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

class HomeView(TemplateView):
    template_name = "index.html"

class LoginView(SuccessMessageMixin, LoginView):
    template_name = 'users/login.html'
    success_message = "Вы залогинены"
    next_page = reverse_lazy('index')

class LogoutView(SuccessMessageMixin, LogoutView):
    next_page = reverse_lazy('index')
    success_message = "Вы разлогинены"

    def dispatch(self, request, *args, **kwargs):
        messages.info(request, self.success_message)
        return super().dispatch(request, *args, **kwargs)
# Проверка rollbar
# def error(request):
#    division_by_zero = 1 / 0
#    return HttpResponse("You shouldn't be seeing this")
