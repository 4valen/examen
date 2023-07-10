from django.shortcuts import render
def crud(request):
    mascotas = mascotas.objects.all()
    context = {'alumnos' : alumnos }
    return render(request,'mascotas/mascotaslist.html', context)