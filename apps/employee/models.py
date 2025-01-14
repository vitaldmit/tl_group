from django.db import models
from django.core.validators import MinValueValidator

from mptt.models import MPTTModel, TreeForeignKey


class Department(MPTTModel):
    name = models.CharField('Название', max_length=100)
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children',
        verbose_name='Родительское подразделение'
    )

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        verbose_name = 'Подразделение'
        verbose_name_plural = 'Подразделения'

    def __str__(self):
        return self.name


class Employee(models.Model):
    full_name = models.CharField('ФИО', max_length=255)
    position = models.CharField('Должность', max_length=100)
    hire_date = models.DateField('Дата приема на работу')
    salary = models.DecimalField(
        'Размер оклада',
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )

    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name='employees',
        verbose_name='Подразделение'
    )

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
        ordering = ['full_name']
        indexes = [
            models.Index(fields=['department']),
            models.Index(fields=['hire_date']),
        ]

    def __str__(self):
        return f"{self.full_name} - {self.position}"