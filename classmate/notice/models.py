from django.db import models
from django.contrib.auth.models import User
from group.models import Group

notice_choices = (('urgent', 'urgent'),
                  ('not urgent', 'not urgent'))

class Notice(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    created_date = models.DateTimeField()
    expiry_date = models.DateTimeField()
    notice_type = models.CharField(max_length=10, choices=notice_choices)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    admin = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class FavouriteNotice(models.Model):
    notice = models.ForeignKey(Notice, on_delete=models.CASCADE)
    user_ids = models.ManyToManyField(User)

    def __str__(self):
        return self.notice.title