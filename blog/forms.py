from django import forms
from .models import MyHero, Comment


class PostFrom(forms.ModelForm):
    class Meta:
        model = MyHero
        fields = (
            'photo', 'name', 'max_health', 'endurance', 'intellegence', 'charizma', 'dexterity', 'wisdom', 'acrobatics',
            'analysis', 'athletics', 'strength', 'perception', 'survival', 'performance', 'intimidation', 'history', 'sleight_hand',
            'magic', 'medicine', 'deception', 'nature', 'insight', 'religic', 'stealth', 'conviction', 'caring',
            'items')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'text')
