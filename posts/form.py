from django import forms
from . import models


class CreatePost(forms.ModelForm):
    class Meta:
        model = models.Person
        fields = ['name', 'age', 'slug', 'banner']
