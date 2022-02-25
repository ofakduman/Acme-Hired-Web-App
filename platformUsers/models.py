from django.db import models

# Create your models here.

class PlatformUser(models.Model):
    git_id = models.IntegerField(default=0)
    name = models.TextField(max_length=200,blank=True, null=True)
    label = models.TextField(max_length=200,blank=True, null=True)
    avatar_url = models.TextField(max_length=200,blank=True, null=True)
    favourite = models.BooleanField(default=False)
    html_url = models.TextField(max_length=200,default="null",blank=True, null=True)
    email = models.TextField(max_length=200,default="null@gmail.com",blank=True, null=True)
    login = models.TextField(max_length=200,default="null",blank=True, null=True)
    public_repos = models.IntegerField(default=0)
    public_gists = models.IntegerField(default=0)
    favourite_star = models.IntegerField(default=0)
    platform_type = models.TextField(max_length=200,default="GitHub")
    company = models.TextField(max_length=100,default="null",blank=True, null=True)
    blog = models.TextField(max_length=100,default="null",blank=True, null=True)
    location = models.TextField(max_length=100,default="null",blank=True, null=True)
    bio = models.TextField(max_length=100,default="null",blank=True, null=True)
    followers = models.IntegerField(default=0)
    following = models.IntegerField(default=0)


    def __str__(self):
        return self.name