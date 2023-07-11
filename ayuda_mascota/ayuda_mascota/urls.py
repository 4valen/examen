"""
URL configuration for ayuda_mascota project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from ayuda_mascota.views import view_index
from ayuda_mascota.views import view_galeria
from ayuda_mascota.views import view_formsdata
from ayuda_mascota.views import view_miindicador
from ayuda_mascota.views import view_contacto
from ayuda_mascota.views import view_region
from ayuda_mascota.views import view_login
from ayuda_mascota.views import view_home
from ayuda_mascota.views import view_nosotros
from ayuda_mascota.views import view_tienda
from ayuda_mascota.views import view_donaciones

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', view_index.index),
    path('', view_index.index),    
    path('galeria/', view_galeria.galeria), 
    path('contacto/', view_contacto.contacto),     
    path('forms-data/', view_formsdata.formsdata),    
    path('forms-data/guardar', view_formsdata.guardar),          
    path('mi-indicador/', view_miindicador.miindicador), 
    path('region', view_region.region), 
    path('login/', view_login.login), 
    path('home/', view_home.home),
    path('nosotros/', view_nosotros.nosotros),
    path('tienda/', view_tienda.tienda),
    path('donaciones/', view_donaciones.donaciones),
    path('logout', view_login.logout),
]
