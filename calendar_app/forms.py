from django import forms
from calendar_app.models import Event

class EventForm(forms.Form):
    title = forms.CharField(label='タイトル', max_length=100)
    description = forms.CharField(label='説明', max_length=100)

