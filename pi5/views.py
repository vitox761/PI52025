from django.core.paginator import Paginator
from django.shortcuts import render

def homePageView(request):
    context ={}
         
    return render(request, "homepage.html")


def conclusaoPageView(request):
    context ={}
         
    return render(request, "conclusao.html")

def resultadoSaoPauloPageView(request):
    context ={}
         
    return render(request, "resultado-saopaulo.html")

def resultadoPiracicabaPageView(request):
    context ={}
         
    return render(request, "resultado-piracicaba.html")

def resultadoTaubatePageView(request):
    context ={}
         
    return render(request, "resultado-taubate.html")

def resultadoSaoCarlosPageView(request):
    context ={}
         
    return render(request, "resultado-saocarlos.html")

def resultadoCamposDeJordaoPageView(request):
    context ={}
         
    return render(request, "resultado-camposdejordao.html")

def resultadoBonifacioPageView(request):
    context ={}
         
    return render(request, "resultado-bonifacio.html")

def resultadoCachoeiraPageView(request):
    context ={}
         
    return render(request, "resultado-cachoeira.html")