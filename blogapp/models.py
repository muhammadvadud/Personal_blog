from django.db import models
from django.contrib.auth.models import User

class Education(models.Model):
    adress = models.TextField()
    name = models.CharField(max_length=255 )
    time = models.CharField (max_length=255, null=True, blank=True)
    start_day = models.DateField()
    desc = models.TextField()
    direc = models.TextField()
    def __str__(self):
        return self.name

class Experience(models.Model):
    adress = models.TextField()
    name = models.CharField(max_length=255)
    time = models.CharField (max_length=255, null=True, blank=True)
    desc = models.TextField()
    direc = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class Setting(models.Model):
    key = models.CharField(max_length=255)
    value = models.TextField()
    def __str__(self):
        return self.key


class Portfolio(models.Model):
    title = models.TextField()
    img = models.ImageField()
    url = models.URLField()
    def __str__(self):
        return self.title


class Blog(models.Model):
    time = models.CharField(max_length=255)
    title = models.TextField()
    img = models.ImageField(upload_to="blog/",default="blog/default",blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True )
    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    def __str__(self):
        return self.name


class About(models.Model):
    name = models.TextField()
    email = models.TextField()
    about = models.TextField()
    age = models.IntegerField()
    phone = models.CharField(max_length=255)
    img = models.ImageField(upload_to="about/",default="about/default")

    instagram_user = models.CharField(max_length=100)
    telegram_user = models.CharField(max_length=100)

    def __str__(self):
        return self.name

