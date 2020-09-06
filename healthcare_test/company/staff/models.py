from django.db import models

# Create your models here.
class Employee(models.Model):
    ename = models.CharField(max_length=100)
    dname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    dob = models.DateField(default='')
    pic = models.ImageField(upload_to='images/',blank=True)
    class Meta:
        ordering = ["-ename"]

    def __str__(self):
        return self.ename


class Department(models.Model):
    dname = models.CharField(max_length=100)
    manager = models.ForeignKey(Employee, on_delete=models.CASCADE)
    class Meta:
        ordering = ["-dname"]

    def __str__(self):
        return self.dname