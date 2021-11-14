from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(contact_us)
admin.site.register(subscription)
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Poster)
admin.site.register(PostView)
admin.site.register(Comment)