from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
	filter_horizontal = ('work',)
@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
	pass
@admin.register(Classroom)
class ClassroomAdmin(admin.ModelAdmin):
	filter_horizontal = ('students',)

@admin.register(Assignment)
class AssinmentAdmin(admin.ModelAdmin):
	pass

# Admin All Interface Change
AS = admin.site
AS.site_header = "Developer Interface"
AS.site_title = "Developer Interface"