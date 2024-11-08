from django.db import models

class PersonalDetail(models.Model):
    name = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='profile_pictures/')
    bio = models.TextField()
    interests = models.TextField()

class Achievement(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()

class Skill(models.Model):
    name = models.CharField(max_length=100)
    level = models.CharField(max_length=100)  # e.g., Beginner, Intermediate, Advanced
