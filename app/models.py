from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from PIL import Image
from multiselectfield import MultiSelectField


#Model post
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



#Model profilu
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='none.jpg', upload_to='profile_pics')

    PRZEDMIOTY_CHOICES = [
    ('brak', 'Brak'),
    ('historia', 'Historia'),
    ('angielski', 'Angielski'),
    ('informatyka', 'Informatyka'),
    ('matematyka', 'Matematyka'),
    ('polski', 'Polski'),
    ]

    MIEJSCOWOSC_CHOICES = [
    ('', 'Brak'),
    ('Warszawa', 'Warszawa'),
    ('Gdynia', 'Gdynia'),
    ('Kraków', 'Kraków'),
    ('Poznań', 'Poznań'),
    ('Wrocław', 'Wrocław'),
    ('Ciechanów', 'Ciechanów'),
    ]

    przedmiot = MultiSelectField(choices=PRZEDMIOTY_CHOICES, default='brak')
    miejscowosc = models.CharField(max_length=30, choices=MIEJSCOWOSC_CHOICES, default='brak')
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

    cena = models.PositiveIntegerField(default='0')
    opis = models.TextField(max_length="500")




#Model zgłoszeń użytkowników
class Report(models.Model):
    user_author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_author')
    user_reported = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_reported')
    message = models.TextField()

    def __str__(self):
        return f'{self.user_author.username} ->  {self.user_reported.username}'

    

    


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



