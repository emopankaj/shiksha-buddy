from django.db import models

from admin_panel.page_models import GenericPage


class MenuItem(models.Model):
    id = models.AutoField(primary_key=True)
    site_id = models.CharField(max_length=50)
    text = models.CharField(max_length=30)


class PageMenuItem(MenuItem):
    page = models.ForeignKey(GenericPage)


class SubMenuItem(MenuItem):
    menus = models.ForeignKey(MenuItem)
