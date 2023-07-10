
from django.shortcuts import render

def crud(request):
    mascotas=mascota.objects.all()
    context ={'mascotas': mascotas}
    return render (request, 'mascotas/mascotas_list.html',context)


def mascotasAdd(request):
    if request.method is not POST:
        
        generos=Genero.objects.all() 
        context={'generos':generos}
        return render(request,'mascotas/mascotas_add.html',context)
    

    else:
        rut=request.POST["rut"]

        nombre=request.POST["nombre"]
        obj=mascota.objects.create(rut=rut)
        obj.save()
        context={'mensaje':"ok , datos guardados"}

        return render(request, ' templates/mascotas_add.html',context)

def mascotas_del(request,pk):
    context={}
    try:
        mascota=mascota.object.get(run,pk)
        mascota.delete()
        mensaje="bien datos eliminados"
        mascota= mascota.objects.all()
        context = {'mascota': mascota, 'mensaje' : mensaje}
        return render(request,'templates/mascota/list.html',context)
    except:
        mensaje="error , rut no existe"
        mascota=mascota.object.all()
        context = {'mascota': mascota, 'mensaje' : mensaje}
        return render(request,'templates/mascota/list.html',context)
    

def mascota_findedit(request,pk ):
    if pk!="":
        mascota=mascota.objects.get(returm)
        genero=genero.object

        print(type(mascota.id_genero.genero))
        context={'mascota':mascota ,'generos':genero}
        if mascota:
            return render(request, 'template/mascota_update.html',context)
        


