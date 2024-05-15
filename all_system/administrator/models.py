from django.db import models
from common.models import Applications, Employes, Files

class AdministratorModel(models.Model):
    applications_common = models.ForeignKey(Applications, on_delete=models.CASCADE)
    employes_common = models.ForeignKey(Employes, on_delete=models.CASCADE)
    files_common = models.ForeignKey(Files, on_delete=models.CASCADE)

class SiteAddEmpModel(models.Model):
    e_id = models.AutoField(primary_key=True)
    login = models.CharField(max_length=15)
    password = models.CharField(max_length=100)
    name = models.CharField(max_length=40, blank=True, null=True)
    email_telephone = models.CharField(max_length=20, blank=True, null=True)
    positionj = models.CharField(default='manager')

    objects = models.Manager()
