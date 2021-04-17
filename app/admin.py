from django.contrib import admin
from .models import Post
from .models import Profile
from .models import Report

admin.site.register(Post)

admin.site.register(Profile)




class ReportAdmin(admin.ModelAdmin):
    fields= ['user_author', 'user_reported', 'message',]
    readonly_fields = ['user_author', 'user_reported', 'message',]

    class Meta:
        model= Report



admin.site.register(Report, ReportAdmin)





 


