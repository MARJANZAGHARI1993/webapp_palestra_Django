from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),  # URL per la homepage
    # ... altri URL per la tua app web_palestra
]