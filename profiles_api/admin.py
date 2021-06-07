from django.contrib import admin
from profiles_api import models

## Models need to be defined to be later used for Admin.
admin.site.register(models.UserProfile)
admin.site.register(models.ProfileFeedItem)
