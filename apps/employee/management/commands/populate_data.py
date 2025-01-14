from django.utils import timezone
from django.db import transaction
from django.core.management.base import BaseCommand

import random
from decimal import Decimal
from datetime import timedelta

from apps.employee.models import Department, Employee


class Command(BaseCommand):
    help = 'Populate database with large number of employees'

    def generate_full_name(self):
        first_names = ['Александр', 'Елена', 'Иван', 'Мария', 'Дмитрий', 'Ольга', 
                      'Сергей', 'Анна', 'Павел', 'Наталья', 'Михаил', 'Екатерина']
        last_names = ['Иванов', 'Петров', 'Сидоров', 'Смирнов', 'Кузнецов', 
                     'Попов', 'Васильев', 'Соколов', 'Михайлов', 'Новиков']
        middle_names = ['Александрович', 'Иванович', 'Петрович', 'Сергеевич',
                       'Дмитриевич', 'Андреевич', 'Алексеевич']

        return f"{random.choice(last_names)} {random.choice(first_names)} {random.choice(middle_names)}"

    def handle(self, *args, **kwargs):
        positions = [
            ('Руководитель', (150000, 300000)),
            ('Ведущий специалист', (120000, 180000)),
            ('Старший специалист', (90000, 140000)),
            ('Специалист', (60000, 100000)),
            ('Младший специалист', (45000, 70000))
        ]

        departments = list(Department.objects.all())

        batch_size = 1000
        total_employees = 50000

        self.stdout.write('Starting employee generation...')

        with transaction.atomic():
            employee_objects = []
            for i in range(total_employees):
                position, salary_range = random.choice(positions)
                hire_date = timezone.now().date() - timedelta(
                    days=random.randint(30, 365 * 5)
                )

                employee = Employee(
                    full_name=self.generate_full_name(),
                    position=position,
                    hire_date=hire_date,
                    salary=Decimal(random.randint(salary_range[0], salary_range[1])),
                    department=random.choice(departments)
                )
                employee_objects.append(employee)

                if len(employee_objects) >= batch_size:
                    Employee.objects.bulk_create(employee_objects)
                    employee_objects = []
                    self.stdout.write(f'Generated {i + 1} employees...')

            if employee_objects:
                Employee.objects.bulk_create(employee_objects)

        self.stdout.write(self.style.SUCCESS(f'Successfully created {total_employees} employees'))
