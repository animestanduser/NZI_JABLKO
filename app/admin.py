from django.contrib import admin
from .models import Post
from .models import Profile
from .models import Report
from .models import Rate
from .models import Auth
from .models import Friend_Request

admin.site.register(Post)

admin.site.register(Profile)

class FriendsAdmin(admin.ModelAdmin):
    fields= ['from_user', 'to_user',]


    class Meta:
        model= Friend_Request

admin.site.register(Friend_Request, FriendsAdmin)

class ReportAdmin(admin.ModelAdmin):
    fields= ['user_author', 'user_reported', 'message',]
    readonly_fields = ['user_author', 'user_reported', 'message',]

    class Meta:
        model= Report



admin.site.register(Report, ReportAdmin)


class RateAdmin(admin.ModelAdmin):
    fields= ['user_rate_author', 'user_rated', 'ocena',]
    readonly_fields = ['user_rate_author', 'user_rated', 'ocena',]

    class Meta:
        model= Rate


admin.site.register(Rate, RateAdmin)


class AuthAdmin(admin.ModelAdmin):
    fields= ['user_auth_author', 'wzor', 'zdjecie',]
    readonly_fields = ['user_auth_author', 'wzor', 'zdjecie',]

    class Meta:
        model= Rate



admin.site.register(Auth, AuthAdmin)





 


