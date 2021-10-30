from django.contrib import admin

from .models import Post
# from pagedown.widgets import AdminPagedownWidget
# from .forms import PostCreateForm
#
#
# class PostFormAdmin(admin.ModelAdmin):
#     form = PostCreateForm
#     fields = ['user',
#               'title',
#               'slug',
#               'description',
#               'image',
#               'category',
#               'view_count',
#               'like',
#               'unlike',
#               'published_date', ]
#
#
# admin.site.register(Post, PostFormAdmin)