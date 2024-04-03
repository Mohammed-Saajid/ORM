from django.db import models as m

class Employee(m.Model):
    empid = m.IntegerField()
    empname = m.CharField(max_length=20)
    dept = m.CharField(max_length=20)
    salary = m.FloatField()
