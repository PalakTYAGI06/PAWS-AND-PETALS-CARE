from django.db import models

# Create your models here.
#from django.contrib.auth.models import AbstractUser
#from django.db import models

#class CustomUser(AbstractUser):
    #full_name = models.CharField(max_length=100)
    #role = models.CharField(max_length=20, choices=[('owner','Pet Owner'),('caretaker','Caretaker')])
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('owner', 'Pet Owner'),
        ('caretaker', 'Caretaker'),
    )

    full_name = models.CharField(max_length=100)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
def __str__(self):
        return self.username





# Create your models here.(camera)


class Snapshot(models.Model):
    image = models.ImageField(upload_to='snapshots/')
    created_at = models.DateTimeField(auto_now_add=True)
    note = models.CharField(max_length=120, blank=True)

    def __str__(self):
        return f"Snapshot {self.id} at {self.created_at:%Y-%m-%d %H:%M}"
#feeback #

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"   