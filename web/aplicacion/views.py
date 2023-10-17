from django.shortcuts import render

def index(request):
    # Lógica de la vista
    return render(request, 'aplicacion/index.html')
