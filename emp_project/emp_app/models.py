from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    role = models.CharField(max_length=100, null=True, blank=True)
    salary = models.FloatField()
    manager = models.ForeignKey('Employee', on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        db_table = 'employee_table'

    def __str__(self):
        return self.name
