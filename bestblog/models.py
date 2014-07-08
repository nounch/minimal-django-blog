from django.db import models
from django.forms import ModelForm
import datetime


class Post(models.Model):
    heading = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    text = models.TextField()
    date = models.DateTimeField(default=datetime.datetime.now)
    publisher = models.ForeignKey('bestblog.User')

    def __unicode__(self):
        return self.heading


class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    nick_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    joining_date = models.DateTimeField('joining date')

    def __unicode__(self):
        return self.first_name + ' ' + self.last_name + '(' + self.nick_name + ')'


class PostForm(ModelForm):
    class Meta:
        model = Post
        exclude = ('date',)

    def __unicode__(self):
        return self.heading

