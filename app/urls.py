from django.urls import path, include
from . import views
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static 
from django.conf import settings
from django.views.generic import TemplateView

urlpatterns = [

    #strona główna(muszą być oba bo inaczej error)
    path('', views.start, name='home'),
    path('', views.start, name='index'),

    #rejestracja i przypominanie hasła
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
#działa
    url(r'^password_change/$', views.change_password, name='change_password'),
    

#działa
    url(r'^accounts/password_reset/$', auth_views.PasswordResetView.as_view(template_name = "registration/password_reset.html"),name ='reset_password'),

#działa
    url(r'^accounts/password_reset/done/$', auth_views.PasswordResetDoneView.as_view(template_name = "registration/password_reset_sent.html"), name ='password_reset_done'),

#działa pod warunkiem, że nie folder "registrations" tylko "accounts" (XD)
    url(r'accounts/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', auth_views.PasswordResetConfirmView.as_view(template_name = "accounts/password_reset_confirm.html"), name ='password_reset_confirm'),
    url(r'^accounts/reset/done/$', auth_views.PasswordResetCompleteView.as_view(template_name = "accounts/password_reset_done.html"), name ='password_reset_complete'),

  

    #Podgląd profilu
    path('profile/<int:user>/', views.profile, name='profile'),
    


    #Szukaj korepetytorów
    path('search/', views.search, name='search'),

    #Lista korepetytorów
    path('list/', views.list, name='list'),

    #Chybił trafił
    path('random/', views.random, name='random'),

    #Edycja przedmiotów oraz miejscowości
    path('edit_personal/', views.edit_personal, name='edit_personal'),

    #Edycja danych osobowych
    path('edit/', views.edit, name='edit'),

    #Report profilu
    path('report/<int:user>/', views.report, name='report'),
    
  
    path('chat/<int:sender>/<int:receiver>/', views.message_view, name='chat'),

    path('api/messages/<int:sender>/<int:receiver>/', views.message_list, name='message-detail'),
    path('api/messages/', views.message_list, name='message-list'),
]
url(r'^app/random.html', TemplateView.as_view(template_name="profile_view.html"),
                   name='random'),

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)