
from django.contrib import admin
from .models import Candidato, Empresa, Vaga, Candidatura

admin.site.register(Candidato)
admin.site.register(Empresa)
admin.site.register(Vaga)
admin.site.register(Candidatura)
