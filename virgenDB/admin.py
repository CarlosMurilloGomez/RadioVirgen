from django.contrib import admin
from virgenDB.models import Autor, Programa, Podcast, Usuario, Reproducciones, Plan, Familia
# Register your models here.
admin.site.register(Programa)
admin.site.register(Autor)
admin.site.register(Plan)
admin.site.register(Podcast)
admin.site.register(Familia)
admin.site.register(Usuario)
admin.site.register(Reproducciones)
