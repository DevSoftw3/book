from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.views import View


from apps.login.forms import CreateUserForm


# def register_page(request):
#     register_form = CreateUserForm
#     if request.method == 'POST':
#         register_form = CreateUserForm(request.POST)
#         if register_form.is_valid():
#             register_form.save()
#     return render(request, 'register.html', {'register_form':register_form})


class RegisterUserView(View):
    template = 'register.html'

    def get(self, request):
        register_form = CreateUserForm
        return render(request, self.template, dict(register_form=register_form))

    def post(self, request):
        register_form = CreateUserForm(request.POST)
        if register_form.is_valid():
            usuario = register_form.save()
            nombre_usuario = register_form.cleaned_data.get('username')
            messages.info(request, f'Bienvenido {nombre_usuario}')
            login(request, usuario)
            # register_form.save()
            # messages.info(request, 'Cuenta creada!')

            return redirect('book:home')
        else:
            for msg in register_form.error_messages:
                messages.error(register_form.error_messages[msg])
            return render(request, self.template, dict(register_form=register_form))


class AccederView(LoginView):
    template_name = 'login.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class CopyrightView(View):
    template = 'copyright.html'

    def get(self, request):
        return render(request, self.template)