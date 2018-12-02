from django import forms

import sys
sys.path.append("..")
from accounts.models import CustomUser

class ReaderModeForm(forms.ModelForm):

    reader_mode = forms.BooleanField(required=False)

    # #status = forms.TypedChoiceField(coerce=int,
    # #                    choices=((1, 'Unlocked'), (0, 'Locked')),
    # #                    widget=forms.RadioSelect())

    class Meta:
        model = CustomUser
        fields = ['reader_mode']
