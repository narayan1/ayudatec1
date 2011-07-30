from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.ForeignKey(User)
    picture = models.ImageField(upload_to='pictures/',blank=True,null=True)
    bio = models.TextField()
    publish_email = models.BooleanField(default=True)

    def __unicode__(self):
        return self.user.username

class Category(models.Model):
    name = models.CharField(max_length=64)
    slug = models.SlugField()

    def __unicode__(self):
        return self.name

class Article(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=256)
    slug = models.SlugField()
    publish_date = models.DateField()
    content = models.TextField()
    category = models.ForeignKey(Category)

    def __unicode__(self):
        return ' - '.join([str(self.user), self.title, str(self.publish_date)])
