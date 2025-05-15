"""
URL configuration for pi5 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePageView, name='home_page'),
    path('conclusao', views.conclusaoPageView, name='conclusao'),
    path('resultadosaopaulo', views.resultadoSaoPauloPageView, name='resultado_saopaulo'),
    path('resultadopiracicaba', views.resultadoPiracicabaPageView, name='resultado_piracicaba'),
    path('resultadotaubate', views.resultadoTaubatePageView, name='resultado_taubate'),
    path('resultadosaocarlos', views.resultadoSaoCarlosPageView, name='resultado_saocarlos'),
    path('resultadocamposdejordao', views.resultadoCamposDeJordaoPageView, name='resultado_camposdejordao'),
    path('resultadobonifacio', views.resultadoBonifacioPageView, name='resultado_bonifacio'),
    path('resultadocachoeira', views.resultadoCachoeiraPageView, name='resultado_cachoeira'),
    path('admin/', admin.site.urls),
]
