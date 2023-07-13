from django.contrib import admin
from .models import Stock, Categoria,detalle_boleta,Boleta

# Register your models here.
admin.site.register(Stock)
admin.site.register(Categoria)
admin.site.register(detalle_boleta)
admin.site.register(Boleta)