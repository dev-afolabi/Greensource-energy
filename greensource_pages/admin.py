from django.contrib import admin
from django.db import models
from .models import Images, Testimonial, Solar, Landingpage

# Register your models here.


admin.site.register(Images)
admin.site.register(Testimonial)
admin.site.register(Solar)
admin.site.register(Landingpage)