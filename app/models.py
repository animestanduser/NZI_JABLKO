from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from PIL import Image



class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    przedmiot = models.TextField(max_length="30")
    opis = models.TextField(max_length="500")
    miejscowosc = models.TextField(max_length="30")
    BOOLEAN_CHOICES = (
        (True, 'Nauczyciel'),
        (False, 'Uczen')
    )
    affinity = models.BooleanField(choices=BOOLEAN_CHOICES)
    users = User.objects.all()
    args = {'users':users,}

    def __str__(self):
        return f'{self.user.username} Profile'
        return f'{self.user.przedmiot} Profile'
        return f'{self.user.opis} Profile'


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)

class displayusername(models.Model):
    username=models.CharField(max_length=30)


class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')
    message = models.CharField(max_length=1200)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return self.message

    class Meta:
        ordering = ('timestamp',)