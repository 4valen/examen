from django.shortcuts import render

def miindicador(request):
    return render(request, 'mi-indicador.html', {'active_miindicador': 'active'})