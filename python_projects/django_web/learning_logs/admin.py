from django.contrib import admin

# 注意要加.
from .models import Topic, Entry

# Register your models here.
admin.site.register(Topic)
admin.site.register(Entry)
