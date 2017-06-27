from django import forms
from .models import *

class OccupationDetailForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Occupation_Detail
        fields = ('owner_name', 'owner_city','owner_state', 'owner_address', 'password')