from django.contrib import admin
from embed_video.admin import AdminVideoMixin
from .models import Recomendacion, Principal, Categoria

# Register your models here.
class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

class RecomendacionAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

class PrincipalAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')


admin.site.register(Recomendacion, RecomendacionAdmin)
admin.site.register(Principal, PrincipalAdmin)
admin.site.register(Categoria, CategoriaAdmin)