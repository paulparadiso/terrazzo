from django import forms
from .models import SyncGroup

class AddToSyncGroupForm(forms.Form):
    _selected_action = forms.CharField(widget=forms.MultipleHiddenInput)
    collection = forms.ModelChoiceField(
        queryset=SyncGroup.objects.all(),
        label="Select SyncGroup",
        empty_label="Choose SyncGroup"
    )