import datetime

from django import forms

from .models import Match

class MatchForm(forms.ModelForm):
    date = forms.DateTimeField(initial=datetime.datetime.now())

    class Meta:
        model = Match
        