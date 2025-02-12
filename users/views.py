from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from users.forms import CustomUserCreationForm
from django.core.mail import send_mail


class RegisterView(CreateView):
    template_name = 'users/register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('catalog:home')

    def form_valid(self, form):
        user = form.save()
        self.send_welcome_email(user.email)
        return super().form_valid(form)

    def send_welcome_email(self, user_email):
        subject = 'Добро пожаловать в наш сервис!'

        message = 'Спасибо, что зарегистрировались в нашем сервисе!'
        from_email = 'lerik131007@yandex.ru'
        recipient_list = [user_email,]
        send_mail(subject, message, from_email, recipient_list)


class LoginView(LoginView):
    template_name = 'users/login.html'
    success_url = reverse_lazy('catalog:home')


class LogoutView(LogoutView):
    template_name = 'users/logout.html'
    next_page = reverse_lazy('catalog:register')

