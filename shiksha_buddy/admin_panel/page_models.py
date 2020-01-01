from django.db import models
from django.db.models import DecimalField


# class Article(models.Model):
#     article_id = models.AutoField(primary_key=True)
#     article_heading = models.CharField(max_length=250)
#     article_body = models.TextField()


class GenericPage(models.Model):
    id = models.AutoField(primary_key=True)
    site_id = models.CharField(max_length=50)
    page_name = models.CharField(max_length=80)
    title = models.CharField(max_length=50, blank=True)
    heading = models.CharField(max_length=250, blank=True)

    class Meta:
        abstract = True


class ContactPage(GenericPage):
    latitude = DecimalField(max_digits=9, decimal_places=6, blank=True, default=None)
    longitude = DecimalField(max_digits=9, decimal_places=6, blank=True)
    address = models.CharField(max_length=250, blank=True)
    phone = models.CharField(max_length=15, blank=True)
    email = models.CharField(max_length=30, blank=True)
    facebook_link = models.CharField(max_length=50, blank=True)
    twitter_link = models.CharField(max_length=50, blank=True)


class TextImagePage(GenericPage):
    image = models.CharField(max_length=100, blank=True)
    text = models.TextField(blank=True)
