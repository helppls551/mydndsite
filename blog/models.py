from django.conf import settings
from django.db import models
from django.utils import timezone


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




    created_time = models.DateTimeField(default=timezone.now)
