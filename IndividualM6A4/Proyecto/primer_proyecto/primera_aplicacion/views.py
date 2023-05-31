from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from .models import Contenido, DatosCliente
from primera_aplicacion.forms.formulariousuario import FormularioUsuarioForm

# Create your views here.
def index_welcome(request):
    return render(request, 'welcome.html')

class UsersApp(TemplateView):
    template_name = "users.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['usuarios'] = User.objects.all()

        return context

class FormUsers(TemplateView):
    template_name = 'form_user.html'
    
    def get_context_data(self, **kwargs):
        contexto = super(FormUsers, self).get_context_data(**kwargs)
        contexto["username"] = self.kwargs["id"]
        contexto["form"] = FormularioUsuarioForm()
        return contexto
    
    def post(self, request,**kwargs):
        print("entro a post")
        form = FormularioUsuarioForm(request.POST)
        if form.is_valid():
            username = self.kwargs["id"]
            direccion = form.cleaned_data["direccion"]
            edad = form.cleaned_data["edad"]
            profesion = form.cleaned_data["profesion"]
            print("Formulario Valido")
            print(username, direccion, edad, profesion)
            datos = DatosCliente(id=username, direccion=direccion, edad=edad, profesion=profesion)
            datos.save()
        else:
            print("Formulario Invalido")
            print(form)
        return redirect('/clientes')
        
    


def contenido(request):
    datos = Contenido.objects.all()
    contexto = {'datos' : datos}

    return render(request, 'contenido.html', contexto)



