from django.db import models

# Create your models here.
from django.db import models

class employee(models.Model):
    emp_name = models.CharField(max_length=100)
    emp_id = models.IntegerField()
    emp_salary = models.FloatField()

    def __str__(self):
        return self.emp_name