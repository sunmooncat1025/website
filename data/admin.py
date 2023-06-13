from django.contrib import admin

# Register your models here.
from .models import Topic,Entry,Data

admin.site.register(Topic)
admin.site.register(Entry)
admin.site.register(Data)