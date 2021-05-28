from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.files.images import get_image_dimensions
from .models import Profile
from .models import Post
from .models import Report
from .models import Rate
from .models import Auth
from .models import Post






class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    first_name = forms.CharField(max_length=30, required=True)

    class Meta:
        model = User
        fields = ('username','first_name', 'email', 'password1', 'password2')


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('opis', 'image','korepetytor', 'miejscowosc')

        widgets = {
            'opis': forms.Textarea(attrs={'class': 'form-control'}),
        }

class ProfileOptionsForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('miejscowosc', 'przedmiot', 'cena')

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ('message',)

    widget = {
            'message': forms.Textarea(attrs={'class':'form-control'}),
    }

class RateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('punkty', 'ranga',)


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rate
        fields = ('ocena',)

    widget = {
            'ocena': forms.Textarea(attrs={'class':'form-control'}),
    }


class AuthForm(forms.ModelForm):
    class Meta:
        model = Auth
        fields = ('wzor', 'zdjecie',)


class AuthProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('wzor', 'zdjecie',)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('text',)

    widget = {
            'text': forms.Textarea(attrs={'class':'form-control'}),
    }
