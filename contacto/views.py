from django.shortcuts import redirect, render
from .forms import FormularioContacto
from django.core.mail import EmailMessage

# Create your views here.

def contacto(request):
    formulario_contacto=FormularioContacto()

    if request.method=="POST":
        formulario_contacto=FormularioContacto(data=request.POST)
        if formulario_contacto.is_valid():
            nombre=request.POST.get("nombre")
            email=request.POST.get("email")
            cargo=request.POST.get("cargo")
            contenido=request.POST.get("contenido")

            email=EmailMessage("Mensaje desde Contacto en Django","El usuario con nombre {} y cargo {} con la dirección {} escribe lo siguiente:\n\n {}".format(nombre, cargo, email, contenido),"",["tfgservidor@gmail.com"],reply_to=[email])
            try:
                email.send()
                return redirect("/contacto/?valido")
            except:
                return redirect("/contacto/?novalido")

    return render(request, "contacto/contacto.html",{"formulario":formulario_contacto})
