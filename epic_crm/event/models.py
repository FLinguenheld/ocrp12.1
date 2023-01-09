from django.db import models
from django.contrib.auth.models import User

from epic_crm.contract.models import Contract


class Event(models.Model):

    name = models.CharField(max_length=150, unique=True)
    informations = models.CharField(max_length=500, blank=True)

    date = models.DateTimeField(blank=True)
    date_created = models.DateTimeField(auto_now_add=True, editable=False)
    date_updated = models.DateField(auto_now=True)

    contract = models.OneToOneField(to=Contract, on_delete=models.CASCADE)

    assigned_user = models.ForeignKey(to=User,
                                      on_delete=models.SET_NULL,
                                      null=True,
                                      blank=True,
                                      default=None)

    def __str__(self):
        return f"Event [ {self.pk} - {self.name} - {self.date} - {self.contract} ]"