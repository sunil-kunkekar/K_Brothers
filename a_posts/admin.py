from django.contrib import admin
from a_posts.models import *

# Register your models here.
admin.site.register(POST)

admin.site.register(Tag)
admin.site.register(Comment)