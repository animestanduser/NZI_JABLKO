from django.urls import path, include
from . import views
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static 
from django.conf import settings

urlpatterns = [

    #strona rejestracji
    path('', views.start, name='home'),

    path('', views.start, name='index'),


    url(r'^signup/$', views.signup, name='signup'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),

    url(r'^password_change/$', views.change_password, name='change_password'),
    


    url(r'^accounts/reset_password/$', auth_views.PasswordResetView.as_view(template_name = "registration/reset_password.html"),name ='reset_password'),


    url(r'^accounts/password_reset/done/$', auth_views.PasswordResetDoneView.as_view(template_name = "registration/password_reset_sent.html"), name ='password_reset_done'),
    
    url(r'^accounts/reset/done/$', auth_views.PasswordResetCompleteView.as_view(template_name = "registration/password_reset_done.html"), name ='password_reset_complete'),

 
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name = "registration/password_reset_form.html"), name ='password_reset_confirm'),
 

  


    path('panel_podglad/', views.panel_podglad, name='panel_podglad'),


    path('find_page/', views.find_page, name='find_page'),

    path('teachers_list/', views.teachers_list, name='teachers_list'),

    path('random_teacher/', views.random_teacher, name='random_teacher'),

    path('personal_information_edit/', views.edit_personal, name='edit_personal'),

    path('personal_information_edit/', views.personal_information_edit_link, name='personal_information_edit_link'),

    path('edit/', views.edit, name='edit'),
    
  

    path('edit/', views.edit_view, name='edit_view'),

    
    
    path('chat/<int:sender>/<int:receiver>/', views.message_view, name='chat'),
    path('api/messages/<int:sender>/<int:receiver>/', views.message_list, name='message-detail'),
    path('api/messages/', views.message_list, name='message-list'),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)