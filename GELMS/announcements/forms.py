from django import forms

from .models import Announcement

class AnnouncementForm(forms.ModelForm):

    class Meta:
        model = Announcement
        fields = ("content",)

class AnnouncementEditForm(forms.ModelForm):

    
    class Meta:
        model = Announcement
        fields = ("content",)

        