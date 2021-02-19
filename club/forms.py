from django import forms
from .models import Resource, Meeting, MeetingMinutes, Event

class MeetingForm(forms.ModelForm):
    class Meta:
        model =  Meeting
        fields = '__all__' 