from django.db import models
from django.contrib.auth.models import User

#description, license, date_upload, date_taken, owner_name, icon_server, original_format, last_update, geo, tags, machine_tags, o_dims, views, media, path_alias, url_sq, url_t, url_s, url_q, url_m, url_n, url_z, url_c, url_l, url_o
# Create your models here.

class FlickUser(models.Model):
    name = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)
    username = models.CharField(max_length=50,null=True,blank=True)
    user = models.ForeignKey(User,null=True, blank=True, default = None)

    def __unicode__(self):
        if self.name:
            return self.name
        else:
            return self.owner

class Image(models.Model):
    photo_id    = models.CharField(max_length=40)
    title       = models.CharField(max_length=60)
    image_url    = models.URLField(max_length=200)
    picture     = models.ImageField(upload_to="pictures/flickr",blank=True)
    description = models.TextField(blank=True)
    date_upload = models.DateTimeField(blank=True,null=True)
    license = models.TextField(blank=True)
    date_taken = models.DateTimeField(blank=True,null=True)
    tags       = models.TextField(blank=True)
    owner = models.ForeignKey(FlickUser)

    def __unicode__(self):
        if self.title:
            return self.title
        else:
            return self.photo_id