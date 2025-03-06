from django.contrib import admin
from .models import Utenti, Insegnanti, Incontri, Discipline, Calendario, AbbonamentiIncontri, Abbonamenti

admin.site.register(Utenti)
admin.site.register(Insegnanti)
admin.site.register(Incontri)
admin.site.register(Discipline)
admin.site.register(Calendario)
admin.site.register(AbbonamentiIncontri)
admin.site.register(Abbonamenti)