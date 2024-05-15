from django.db import models
from common.models import Applications, Employes, Files

class UserModel(models.Model):
    applications_common = models.ForeignKey(Applications, on_delete=models.CASCADE)
    employes_common = models.ForeignKey(Employes, on_delete=models.CASCADE)
    files_common = models.ForeignKey(Files, on_delete=models.CASCADE)
