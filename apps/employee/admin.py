from django.contrib import admin

from mptt.admin import DraggableMPTTAdmin

from .models import Department, Employee


@admin.register(Department)
class DepartmentAdmin(DraggableMPTTAdmin):
    list_display = ('tree_actions', 'indented_title')
    list_display_links = ('indented_title',)
    search_fields = ('name',)
    mptt_level_indent = 20


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'position', 'department', 'hire_date', 'salary')
    list_filter = ('department', 'hire_date')
    search_fields = ('full_name', 'position')
    date_hierarchy = 'hire_date'
    ordering = ('full_name',)

