from django.urls import path
from . import views
from django.conf.urls import url
from django.contrib.auth import views as auth_views

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
]
