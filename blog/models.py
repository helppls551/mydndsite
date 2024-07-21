from django.conf import settings
from django.db import models
from django.utils import timezone
from . import func

class MyHero(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="photos/")
    name = models.CharField(max_length=25)
    strength = models.IntegerField()
    endurance = models.IntegerField()
    intellegence = models.IntegerField()
    charizma = models.IntegerField()
    dexterity = models.IntegerField()
    wisdom = models.IntegerField()
    acrobatics = models.BooleanField()
    analysis = models.BooleanField()
    athletics = models.BooleanField()
    perception = models.BooleanField()
    survival = models.BooleanField()
    performance = models.BooleanField()
    intimidation = models.BooleanField()
    history = models.BooleanField()
    sleight_hand = models.BooleanField()
    magic = models.BooleanField()
    medicine = models.BooleanField()
    deception = models.BooleanField()
    nature = models.BooleanField()
    insight = models.BooleanField()
    religic = models.BooleanField()
    stealth = models.BooleanField()
    conviction = models.BooleanField()
    caring = models.BooleanField()
    max_health = models.IntegerField()
    items = models.TextField(default='Ваше Снаряжение')
    created_time = models.DateTimeField(default=timezone.now)

class Comment(models.Model):
    post = models.ForeignKey('blog.MyHero', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()
