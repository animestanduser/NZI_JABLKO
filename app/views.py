from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.http import HttpResponse
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from django import forms
from .forms import SignupForm 
from django.views import generic
from django.contrib.auth.forms import UserChangeForm
from django.http import HttpResponseRedirect
from .models import Profile
from .forms import UserEditForm, ProfileEditForm, ProfileOptionsForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django.shortcuts import render
from .models import displayusername
from django.http.response import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Message
from .serializers import MessageSerializer, UserSerializer




def main_tlo(request):
        return render(request, 'app/main_tlo.html',
                      {'users': User.objects.exclude(username=request.user.username)})



    

def start(request):
    return render(request, 'app/start.html',)

def panel(request):
    return render(request, 'app/panel.html',)

def personal_information_edit_link(request):
    if request.method == "GET":
            return render(request, 'app/personal_information_edit.html', {'users': User.objects.exclude(username=request.user.username)})
    

def base(request):
    return redirect('base',)

def index(request):
        if request.method == "GET":
            return render(request, 'app/index.html', {'users': User.objects.exclude(username=request.user.username)})

def find_page(request):
    return render(request, 'app/find_page.html',)

def teachers_list(request):
    if request.method == "GET":
            return render(request, 'app/teachers_list.html', {'users': User.objects.exclude(username=request.user.username)})

def random_teacher(request):
    if request.method == "GET":
            return render(request, 'app/random_teacher.html', {'users': User.objects.exclude(username=request.user.username)})

def panel_podglad(request):
    if request.method == "GET":
            return render(request, 'app/panel_podglad.html', {'users': User.objects.exclude(username=request.user.username)})

def profile_edit(request):
    return render(request, 'app/profile_edit.html',)

def pokazpanel(request):
    return render(request, 'app/edit.html')

def pokazliste(request):
    return render(request, 'app/account_list.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            
          # profile = Profile.objects.create(user=new_user)
            current_site = get_current_site(request)
            mail_subject = 'Aktywuj swoje konto na Korepder'
            message = render_to_string('registration/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
            return render(request, 'registration/signup_succes.html', {'form': form})
    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {'form': form})



def activate(request, uidb64, token, backend='django.contrib.auth.backends.ModelBackend'):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        return HttpResponse('Aktywacja przebiegła pomyślnie')
    else:
        return HttpResponse('Aktywacja jest błędna!')



def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  
            return render(request, 'registration/change_password_succes.html', {'form': form})
        else:
            return render(request, 'registration/change_password_failed.html', {'form': form})
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'registration/change_password.html', {
        'form': form
    })


@csrf_exempt
def message_list(request, sender=None, receiver=None):
    if request.method == 'GET':
        messages = Message.objects.filter(sender_id=sender, receiver_id=receiver, is_read=False)
        serializer = MessageSerializer(messages, many=True, context={'request': request})
        for message in messages:
            message.is_read = True
            message.save()
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MessageSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)





def message_view(request, sender, receiver):
    if not request.user.is_authenticated:
        return redirect('index')
    if request.method == "GET":
        return render(request, "app/messages.html",
                      {'users': User.objects.exclude(username=request.user.username),
                       'receiver': User.objects.get(id=receiver),
                       'messages': Message.objects.filter(sender_id=sender, receiver_id=receiver) |
                                   Message.objects.filter(sender_id=receiver, receiver_id=sender)})

@login_required
def edit(request):
    if request.method == 'POST':

        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request, 'app/edit.html', {'users': User.objects.exclude(username=request.user.username),'user_form': user_form, 'profile_form': profile_form})


@login_required
def edit_personal(request):
    if request.method == 'POST':

        profile_settings_form = ProfileOptionsForm(instance=request.user.profile, data=request.POST, files=request.FILES)

        if profile_settings_form.is_valid():
            profile_settings_form.save()
    else:
        profile_settings_form = ProfileOptionsForm(instance=request.user.profile)
    return render(request, 'app/personal_information_edit.html', {'profile_settings_form': profile_settings_form, 'users': User.objects.exclude(username=request.user.username)})


def chat_view(request):
    if not request.user.is_authenticated:
        return redirect('index')
    if request.method == "GET":
        return render(request, 'app/chat.html',
                      {'users': User.objects.exclude(username=request.user.username)})

def przedmiot_view(request):
    if not request.user.is_authenticated:
        return redirect('index')
    if request.method == "GET":
        return render(request, 'app/panel_podglad.html',
                      {'users': User.objects.exclude(username=request.user.username)})

def edit_view(request):
    if request.method == "GET":
        return render(request, 'app/edit.html',{'users': User.objects.exclude(username=request.user.username)})  
    if not request.user.is_authenticated:
        return redirect('index')
      


def showlist(request):
    displaynames=User.objects.all()
    return render(request, 'account_list.html',{"displayusername":displaynames})
