from django.contrib import admin

from higiapostquiz.models import ContentCategory, Post, Question

# Register your models here.

admin.site.register(ContentCategory)
admin.site.register(Post)
admin.site.register(Question)