from django.shortcuts import render
from .models import utenti  # Importa il modello con la 'u' minuscola

def index(request):
    return render(request, 'index.html')