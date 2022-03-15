from django.contrib import admin
from .models import CustomUser,Postfile,TwitterKey
# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Postfile)
admin.site.register(TwitterKey)
