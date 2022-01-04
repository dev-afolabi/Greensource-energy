from django.contrib import admin
from django.db import models
from .models import Images, Testimonial, Solar

# Register your models here.


admin.site.register(Images)
admin.site.register(Testimonial)
admin.site.register(Solar)
