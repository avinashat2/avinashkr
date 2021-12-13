from django.contrib import admin

from home.models import Comment, Course, Post, Student

# Register your models here.
admin.site.register(Course)
admin.site.register(Student)

admin.site.register(Post)
admin.site.register(Comment)