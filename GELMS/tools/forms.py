from django import forms
from .models import Tool

class ToolForm(forms.ModelForm):

    status = forms.BooleanField(required=False)

    #status = forms.TypedChoiceField(coerce=int,
    #                    choices=((1, 'Unlocked'), (0, 'Locked')),
    #                    widget=forms.RadioSelect())

    class Meta:
        model = Tool
        fields = ['status']
