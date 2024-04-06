from django.db import models

class Event(models.Model):
    name = models.TextField(verbose_name="name (what you want this event to be called in the admin interface)")
    title = models.TextField()
    desc = models.TextField(verbose_name="description")
    img = models.ImageField(upload_to = "events/", verbose_name="image")

    def __str__(self):      # called when trying to convert a model instance to a str, such as when displaying it in the admin interface
        return self.name
    
class Team(models.Model):
    name = models.TextField()
    title = models.TextField()
    bio = models.TextField()
    img = models.ImageField(upload_to = "team/", verbose_name="image")

    def __str__(self):      # called when trying to convert a model instance to a str, such as when displaying it in the admin interface
        return self.name
    
class Branch(models.Model):
    name = models.TextField(verbose_name="name (what you want this event to be called in the admin interface)")
    title = models.TextField(verbose_name="title (example: US-UT: Provo)")
    desc = models.TextField(verbose_name="description (example: Evan Smith (Brigham Young University))")
    img = models.ImageField(upload_to = "branches/", verbose_name="image")

    def __str__(self):      # called when trying to convert a model instance to a str, such as when displaying it in the admin interface
        return self.name