from django.contrib import admin
from .models import Topic, Entry

admin.site.register(Topic) #Сообщает Django что управление моделью должно осуществляться через административный сайт
admin.site.register(Entry)

# Register your models here.
