from django import forms
from django.forms import ModelForm
from common.models import Applications, Files
from user.models import UserModel

class ApplicationForm(ModelForm):
    class Meta:
        model = Applications
        fields = ['application_text', 'prop_solution', 'name', 'email']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'anonim'}),
            'email': forms.EmailInput(attrs={'placeholder': 'email@example.com'}),
        }

    def __init__(self, *args, **kwargs):
        super(ApplicationForm, self).__init__(*args, **kwargs)
        self.fields['name'].required = False
        self.fields['email'].required = False

    def save(self, commit=True):
        instance = super(ApplicationForm, self).save(commit=False)
        if not instance.name:
            instance.name = 'anonim'
        if commit:
            instance.save()
        return instance


class FileForm(ModelForm):
    class Meta:
        model = Files
        fields = ['path']