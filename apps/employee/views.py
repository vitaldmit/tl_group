from django.views.generic import ListView
from django.http import JsonResponse
from django.template.loader import render_to_string

from .models import Department, Employee


class DepartmentTreeView(ListView):
    model = Department
    template_name = 'employee/department_tree.html'
    context_object_name = 'departments'

    def get_queryset(self):
        return Department.objects.all().select_related('parent').prefetch_related('employees')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['employees_total'] = Employee.objects.count()
        return context


def load_employees(request, department_id):
    page = int(request.GET.get('page', 1))
    per_page = 50
    start = (page - 1) * per_page
    end = start + per_page
    
    employees = Employee.objects.filter(department_id=department_id)[start:end]
    total_employees = Employee.objects.filter(department_id=department_id).count()
    
    html = render_to_string('employee/employee_list_partial.html', {
        'employees': employees,
        'department_id': department_id,
        'has_more': total_employees > end,
        'next_page': page + 1
    })

    return JsonResponse({'html': html})
