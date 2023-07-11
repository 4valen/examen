from django.shortcuts import render

def contacto(request):
    
    return render(request, 'contacto.html', {'active_contacto': 'active'})