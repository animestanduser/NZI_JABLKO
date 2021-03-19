from django.contrib import admin
from .models import Post
from .models import Profile

admin.site.register(Post)

admin.site.register(Profile)

class ProfileAdmin(admin.ModelAdmin):
 list_display = ['user', 'opis', 'image', 'first_name', 'last_name', 'miejsowosc', 'przedmiot']