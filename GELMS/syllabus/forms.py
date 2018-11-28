from django import forms
from .models import Syllabus
from django.contrib.admin import widgets

class DateInput(forms.DateInput):
    input_type = 'date'


class SyllabusForm(forms.ModelForm):

    #due_date = forms.DateField(widget = forms.SelectDateWidget())

    class Meta:
        model = Syllabus
        fields = ['content','due_date',]
        widgets = {'due_date': DateInput()}


class SyllabusEditForm(forms.ModelForm):

    class Meta:
        model = Syllabus
        fields = ['content','due_date',]
        widgets = {'due_date': DateInput()}
