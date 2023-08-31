from django.contrib import admin

from higiapostquiz.models import ContentCategory, Post, Question

admin.site.register(ContentCategory)
admin.site.register(Post)
admin.site.register(Question)