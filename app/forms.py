from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.files.images import get_image_dimensions
from .models import Profile
from .models import Post







class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    affinity = forms.BooleanField(widget=forms.RadioSelect(choices=[(True, 'nauczyciel'),(False, 'uczeń')]))

    class Meta:
        model = User
        fields = ('username','first_name',  'email', 'password1', 'password2', 'affinity')


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('opis', 'image', 'przedmiot', 'miejscowosc', 'affinity')

        widgets = {
            'affinity': forms.RadioSelect(choices=[(True, 'nauczyciel'),(False, 'uczeń')]),
            'opis': forms.TextInput(attrs={'class':'myfieldclass'}),
            'przedmiot': forms.TextInput(attrs={'class':'myfieldclass'}),
            'miejscowosc': forms.TextInput(attrs={'class':'myfieldclass'})
        }