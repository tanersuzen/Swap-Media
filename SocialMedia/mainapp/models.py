from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Profile(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    profile_image = models.ImageField(blank=True, upload_to='images/', null=True)
    cover_image=models.ImageField(blank=True, upload_to='images/', null=True)
    email=models.EmailField(max_length=250, null=True)
    age=models.IntegerField(validators=[MaxValueValidator(120),MinValueValidator(12)], null=True)
    info=models.TextField(blank=True, null=True)


    def __str__(self):
        return f"Profile: {self.username} E-mail: {self.email} Age: {self.age} Info: {self.info}" 