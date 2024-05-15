from django import forms
from django.forms import ModelForm
from common.models import Employes
from .models import AdministratorModel
from administrator.models import SiteAddEmpModel

class NewEmployeeForm(ModelForm):
    class Meta:
        model = SiteAddEmpModel
        fields = ['positionj', 'name', 'email_telephone', 'login', 'password']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'сотрудник'}),
            'email_telephone': forms.EmailInput(attrs={'placeholder': 'email@example.com'}),
        }

    def __init__(self, *args, **kwargs):
        super(NewEmployeeForm, self).__init__(*args, **kwargs)
        self.fields['name'].required = False
        self.fields['email_telephone'].required = False

    def save(self, commit=True):
        instance = super(NewEmployeeForm, self).save(commit=False)
        if not instance.name:
            instance.name = 'сотрудник'
        if commit:
            instance.save()
        return instance