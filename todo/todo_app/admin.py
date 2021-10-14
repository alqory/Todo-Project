from django.contrib import admin
from .models import todo
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ['waktu']

admin.site.register(todo, PostAdmin)