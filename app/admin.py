from django.contrib import admin
from .models import Post
from .models import Profile
from .models import Report
from .models import Rate
from .models import Auth
from .models import Meeting
from django.utils.safestring import mark_safe

admin.site.register(Post)

class ProfileAdmin(admin.ModelAdmin):
    fields= ['user', 'image', 'image_image', 'wzor', 'zdjecie', 'zweryfikowany', 'przedmiot', 'miejscowosc', 'cena', 'punkty', 'ranga', 'opis', 'korepetytor',]
    readonly_fields = ['image_image',]
    search_fields = ['user__username',]

    def image_image(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url = obj.image.url,
            width=200,
            height=200,
            )
    )

    class Meta:
        model= Profile

admin.site.register(Profile, ProfileAdmin)


class MeetingAdmin(admin.ModelAdmin):
    fields= ['tutor', 'council','meeting_title', 'planned_date']


    class Meta:
        model= Meeting

admin.site.register(Meeting, MeetingAdmin)

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
    fields= ['user_auth_author', 'wzor', 'zdjecie', 'wzor_image', 'zdjecie_image',]
    readonly_fields = ['user_auth_author', 'wzor', 'zdjecie', 'wzor_image', 'zdjecie_image',]

    def zdjecie_image(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url = obj.zdjecie.url,
            width=200,
            height=200,
            )
    )

    def wzor_image(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url = obj.wzor.url,
            width=200,
            height=200,
            )
    )
    class Meta:
        model= Rate



admin.site.register(Auth, AuthAdmin)





 


