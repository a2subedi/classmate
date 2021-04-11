from django.db import models
from django.contrib.auth.models import User


class Group(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    key = models.CharField(max_length=20)
    created_date = models.DateTimeField()
    admin = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class LinkUserGroup(models.Model):
    group_id = models.ForeignKey(Group, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)