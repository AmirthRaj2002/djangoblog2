from django.contrib import admin
from .models import Author, Comments,Teacher,Post
# Register your models here.
admin.sites.site.register(Author)
admin.sites.site.register(Teacher)
admin.sites.site.register(Post)
admin.sites.site.register(Comments)
