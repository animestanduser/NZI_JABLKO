from django.contrib import admin
from .models import Post
from .models import Profile
from .models import Report

admin.site.register(Post)

admin.site.register(Profile)

admin.site.register(Report)

class ProfileAdmin(admin.ModelAdmin):
 list_display = ['user', 'opis', 'image', 'first_name', 'last_name', 'miejsowosc', 'przedmiot']