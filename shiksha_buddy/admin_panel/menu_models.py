from django.db import models
from django_mysql.models import JSONField


class MenuItem(models.Model):
    id = models.AutoField(primary_key=True)
    site_id = models.CharField(max_length=50)
    children = JSONField()
