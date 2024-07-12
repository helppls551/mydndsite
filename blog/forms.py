from django import forms
from .models import MyHero


class PostFrom(forms.ModelForm):
    class Meta:
        model = MyHero
        fields = ('photo', 'name','max_health','endurance', 'intellegence', 'charizma', 'dexterity', 'wisdom','acrobatics','analysis','athletics', 'strength', 'perception','survival','performance','history','sleight_hand','magic','medicine','deception','nature','insight','religic','stealth','conviction','caring','items')
