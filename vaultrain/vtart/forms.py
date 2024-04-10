from django import forms
from.models import VaultTrain

class UserFormInput(forms.ModelForm):
    class Meta:
        model = VaultTrain
        fields = ['name', 'submap', 'destination', 'logo', 'time']