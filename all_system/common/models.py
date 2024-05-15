from django.db import models
from datetime import datetime

class Applications(models.Model):
    a_id = models.BigAutoField(primary_key=True)
    application_num = models.CharField(max_length=16, default='1')
    status = models.CharField(max_length=15, default='open')
    datetime = models.DateTimeField(default=datetime.now())
    name = models.CharField(max_length=30, default='anonim')
    application_text = models.CharField(max_length=300, blank=True, null=True)
    prop_solution = models.CharField(max_length=300, blank=True, null=True)
    answer = models.CharField(max_length=300, blank=True, null=True)
    manager = models.ForeignKey('employes', on_delete=models.RESTRICT, blank=True, null=True)
    email = models.CharField(max_length=30, blank=True, null=True)

    objects = models.Manager()

    class Meta:
        managed = False
        db_table = 'applications'


class Employes(models.Model):
    e_id = models.AutoField(primary_key=True)
    login = models.CharField(max_length=15)
    password = models.CharField(max_length=100)
    name = models.CharField(max_length=40, blank=True, null=True)
    email_telephone = models.CharField(max_length=20, blank=True, null=True)
    positionj = models.BooleanField(default=False)

    objects = models.Manager()

    class Meta:
        managed = False
        db_table = 'employes'


class Files(models.Model):
    f_id = models.BigAutoField(primary_key=True)
    application = models.ForeignKey(Applications, on_delete=models.RESTRICT)
    owner = models.BooleanField()
    path = models.CharField(max_length=255)
    
    objects = models.Manager()

    class Meta:
        managed = False
        db_table = 'files'

