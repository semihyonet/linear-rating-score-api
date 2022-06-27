from django.db import models

# Create your models here.


class AbstractModel(models.Model):

    objects = models.Manager()

    class Meta:
        abstract = True
