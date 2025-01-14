from django.urls import path

from .views import DepartmentTreeView
from .views import load_employees


app_name = 'employee'

urlpatterns = [
    path('', DepartmentTreeView.as_view(), name='department_tree'),
    path('load-employees/<int:department_id>/', load_employees, name='load_employees'),
]

