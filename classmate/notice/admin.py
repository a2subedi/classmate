from django.contrib import admin

from .models import Notice, FavouriteNotice

admin.site.register(Notice)
admin.site.register(FavouriteNotice)
