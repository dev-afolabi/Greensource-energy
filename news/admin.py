from django.forms import Textarea,TextInput
from django.db import models
from django.contrib import admin
from .models import Category,Post

# Register your models here.
class MyModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
            models.CharField:{'widget': TextInput(attrs={'size':90})},
            models.TextField:{'widget': Textarea(attrs={'rows':25, 'cols':90})},
        }


admin.site.register(Category)
admin.site.register(Post,MyModelAdmin)

