from django import forms
from .models import MyHero


class PostFrom(forms.ModelForm):
    class Meta:
        model = MyHero
        fields = ('photo', 'name', 'strength', 'endurance', 'intellegence', 'charizma', 'dexterity', 'wisdom',)
