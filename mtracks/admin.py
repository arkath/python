from django.contrib import admin

# Register your models here.

from models import Genres,Track

admin.site.register(Genres)
admin.site.register(Track)
