import re
from django.shortcuts import render
from.models import Categoria, Principal, Recomendacion

# Create your views here.

def recomendacion(request):
    ctx={}
    cat = Categoria.objects.all()
    princ= Principal.objects.all()
    recom= Recomendacion.objects.all()
    cats=[]
    res=[]

    #for r in recom:
        #print(r)
        #print(r.princ.nombre)

    if request.method=="POST":
        
        ctx={"post":"Sí"}
        ctx["cat"]=Categoria.objects.all()
        ctx["princ"]=Principal.objects.all()
        
        for p in Principal.objects.all():
            if request.POST.get(p.__str__(), False):
                ctx.pop("post",0)
                ctx[p.__str__()]="Sí"
                for r in recom:
                    if r.princ.nombre == p.__str__():
                        res.append(r)
                        cats.append(r.princ)
                        print(r.princ.nombre + " " + r.titulo)
                new_set=set(cats)
                cats=list(new_set)
                ctx["cats"]=cats
                ctx["res"]=res
                
                
                
        
            
            
        

        #for p in princ:
        #    print(p.__str__() + " " + p.categ.nombre)
        
        #ctx["cat"]=cat
        #ctx["princ"]=princ
        #print("HOLAAAAA")
        #print(ctx)
        #print("Nginx" in ctx)
        print("ESTOY ENVIANDO:")
        print(ctx)
        return render(request,'recomendaciones/recomendations.html',ctx)
    return render(request,'recomendaciones/recomendations.html',{"post":"No","cat":Categoria.objects.all(), "princ":Principal.objects.all()})
