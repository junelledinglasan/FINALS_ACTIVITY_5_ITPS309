from django.contrib import admin
from .models import TestingDatabase,Subjects,Course,Grades,Notification,Attendance

admin.site.register(TestingDatabase)
admin.site.register(Subjects)
admin.site.register(Course)
admin.site.register(Grades)
admin.site.register(Notification)
admin.site.register(Attendance)