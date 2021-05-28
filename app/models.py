from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from PIL import Image
import random
from multiselectfield import MultiSelectField

#Model post
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    user_commented = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_commented')
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return f'{self.author.username} ->  {self.user_commented.username} ({self.text})'


class Meeting(models.Model):
    tutor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tutor')
    council = models.ForeignKey(User, on_delete=models.CASCADE, related_name='council')
    meeting_title = models.CharField(max_length=30)
    meeting_description = models.TextField()
    planned_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.save()

    
    def __str__(self):
        return f'{self.tutor.username} ->  {self.council.username} ({self.meeting_title},{self.meeting_description})'

#Model profilu
class Profile(models.Model):


    def random_string():
        return "gest" + str(random.randint(1, 5)) + ".png"


    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='none.jpg', upload_to='profile_pics')

    wzor = models.ImageField(default=random_string, upload_to='profile_auth')
    zdjecie = models.ImageField(default='none.jpg', upload_to='profile_auth')

    PRZEDMIOTY_CHOICES = [
    ('brak', 'Brak'),
    ('historia', 'Historia'),
    ('angielski', 'Angielski'),
    ('informatyka', 'Informatyka'),
    ('matematyka', 'Matematyka'),
    ('polski', 'Polski'),
    ]

    MIEJSCOWOSC_CHOICES = [
    ('brak', 'Brak'),
    ('Warszawa', 'Warszawa'),
    ('Gdynia', 'Gdynia'),
    ('Kraków', 'Kraków'),
    ('Poznań', 'Poznań'),
    ('Wrocław', 'Wrocław'),
    ('Ciechanów', 'Ciechanów'),
    ]

    RANGA_CHOICES = [
    ('brak', 'Brak (0-1199)'),
    ('wood', 'Wood (1200-1399)'),
    ('leaf', 'Leaf (1400-1599)'),
    ('gold', 'Gold (1600-1799)'),
    ('diamond', 'Diamond (1800-)'),
    ]

    zweryfikowany = models.BooleanField(default=False)
    przedmiot = MultiSelectField(choices=PRZEDMIOTY_CHOICES, default='brak')
    miejscowosc = models.CharField(max_length=30, choices=MIEJSCOWOSC_CHOICES, default='brak')
    cena = models.PositiveIntegerField(default='0')
    punkty = models.CharField(max_length=7, default=1000)
    ranga = models.CharField(max_length=30, choices=RANGA_CHOICES, default="brak")
    opis = models.TextField(max_length="500", default='Uzupełnij opis aby Twój profil cieszył się większą popularnością.')
    korepetytor = models.BooleanField(default=False)
    users = User.objects.all()
    args = {'users':users,}

    def __str__(self):
        return f'{self.user.username} - Profil'


   
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)



#Model zgłoszeń użytkowników
class Report(models.Model):
    user_author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_author')
    user_reported = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_reported')
    message = models.TextField()

    def __str__(self):
        return f'{self.user_author.username} ->  {self.user_reported.username} ({self.message})'





#Model ocen użytkowników
class Rate(models.Model):
    user_rate_author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_rate_author')
    user_rated = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_rated')
    ocena = models.CharField(max_length=7)

    def __str__(self):
        return f'{self.user_rate_author.username} ->  {self.user_rated.username} ({self.ocena})'


def random_string():
    return "gest" + str(random.randint(1, 5)) + ".png"



#Model weryfikacji
class Auth(models.Model):
    user_auth_author = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_auth_author')
    wzor = models.ImageField(default=random_string, upload_to='profile_auth')
    zdjecie = models.ImageField(default='none.jpg', upload_to='profile_auth')

    def __str__(self):
        return f'{self.user_auth_author.username}'


   

    

    


#Model wiadomości
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





