from django.contrib import admin
from .models import DernierPublication, Imagepricipale, Entete, Menbre, Blog
# Register your models here.

class context(admin.ModelAdmin):
    list_display = ('name', 'description', 'date', 'image')

class context2(admin.ModelAdmin):
    list_display = ('name', 'image')
    
class context3(admin.ModelAdmin):
    list_display = ('titre1', 'titre2', 'image')
    
class context4(admin.ModelAdmin):
    list_display = ('name','domaine','fonction', 'facebook','whatsapp','photo','phone')

class context5(admin.ModelAdmin):
    list_display = ('titre', 'description', 'photo', 'date')   
    
admin.site.register(DernierPublication, context)
admin.site.register(Imagepricipale, context2)
admin.site.register(Entete, context3)
admin.site.register(Menbre, context4)
admin.site.register(Blog, context5)
