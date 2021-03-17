from django.urls import path, include
from . import views
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static 
from django.conf import settings

urlpatterns = [

    #strona rejestracji
    path('', views.start, name='start'),



    path('', views.base, name='base'),
    url(r'^$', views.base, name='home'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),

    url(r'^password_change/$', views.change_password, name='change_password'),
    


    url(r'^accounts/reset_password/$', auth_views.PasswordResetView.as_view(template_name = "registration/reset_password.html"),name ='reset_password'),


    url(r'^accounts/password_reset/done/$', auth_views.PasswordResetDoneView.as_view(template_name = "registration/password_reset_sent.html"), name ='password_reset_done'),
    
    url(r'^accounts/reset/done/$', auth_views.PasswordResetCompleteView.as_view(template_name = "registration/password_reset_done.html"), name ='password_reset_complete'),

 
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name = "registration/password_reset_form.html"), name ='password_reset_confirm'),
    
    
    path('panel/', views.panel, name='panel'),

    path('main_tlo/', views.main_tlo, name='main_tlo'),


    path('panel_podglad/', views.panel_podglad, name='panel_podglad'),

    path('profile_edit/', views.profile_edit, name='profile_edit'),

    path('find_page/', views.find_page, name='find_page'),

    path('teachers_list/', views.teachers_list, name='teachers_list'),

    path('random_teacher/', views.random_teacher, name='random_teacher'),

    path('personal_information_edit/', views.personal_information_edit, name='personal_information_edit'),

    path('edit/', views.edit, name='edit'),

    path('account_list/', views.showlist),

    path('index/', views.index, name='index'),
    
    path('main_tlo/', views.main_tlo, name='chats'),

    path('edit/', views.edit_view, name='edit_view'),

    path('personal_information_edit/', views.edit_personal, name='edit_personal'),

    path('panel_podglad/', views.przedmiot_view, name='przedmioty'),
    path('chat/<int:sender>/<int:receiver>/', views.message_view, name='chat'),
    path('api/messages/<int:sender>/<int:receiver>/', views.message_list, name='message-detail'),
    path('api/messages/', views.message_list, name='message-list'),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)