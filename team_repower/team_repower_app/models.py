from django.db import models

class UserProfile(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()
    skills = models.CharField(max_length=200)
    experience = models.TextField()

    def __str__(self):
        return self.full_name

