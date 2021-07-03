from django.contrib import admin
from schooling.models import Student, Course, Matriculation


class Students(admin.ModelAdmin):
    list_display = ('id', 'name', 'personal_id', 'personal_doc', 'birthday')
    list_display_links = ('id', 'name')
    search_fields = ('name', )
    list_per_page = 20


admin.site.register(Student, Students)


class Courses(admin.ModelAdmin):
    list_display = ('id', 'course_code', 'description', 'level')
    list_display_links = ('id', 'course_code')
    search_fields = ('course_code', )
    list_per_page = 20


admin.site.register(Course, Courses)


class Matriculations(admin.ModelAdmin):
    list_display = ('id', 'student', 'course', 'period')
    list_display_links = ('id', )


admin.site.register(Matriculation, Matriculations)
# Register your models here.
