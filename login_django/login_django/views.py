from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def mostrar_index(request):
    user = request.user
    context = {
        'user': user,
          # Suponiendo que tienes un modelo UserProfile asociado al usuario
        # Otros datos que desees pasar a la plantilla
    }
    return render(request, 'index.html', context)