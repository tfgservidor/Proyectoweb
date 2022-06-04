from django.shortcuts import render, HttpResponse



# Create your views here.

def home(request):

    return render(request, "ProyectoWebApp/home.html")



def tienda(request):

    return render(request, "ProyectoWebApp/tienda.html")





def recomendaciones(request):
    
    if request.method=="POST":
        ctx={"post":"Sí"}
        
        if request.POST.get('app', False):
            ctx.pop("post",0)
            ctx["app"]="Sí"
            

        if request.POST.get('webapp', False):
            ctx.pop("post",0)
            ctx["webapp"]="Sí"
            

        if request.POST.get('ordenador', False):
            ctx.pop("post",0)
            ctx["ordenador"]="Sí"
            

        if request.POST.get('usuario', False):
            ctx.pop("post",0)
            ctx["usuario"]="Sí"
            

        if request.POST.get('servidor', False):
            ctx.pop("post",0)
            ctx["servidor"]="Sí"

        
        
        return render(request,"ProyectoWebApp/recomendaciones.html",ctx)


    return render(request,"ProyectoWebApp/recomendaciones.html",{"post":"No"})