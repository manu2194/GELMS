from django import forms
from .models import Syllabus

class SyllabusForm(forms.ModelForm):

    due_date = forms.DateField(widget = forms.SelectDateWidget())

    class Meta:
        model = Syllabus
        fields = ("content","due_date",)


class SyllabusEditForm(forms.ModelForm):


    class Meta:
        model = Syllabus
        fields = ("content","due_date",)
