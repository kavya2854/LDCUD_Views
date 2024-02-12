from django.db import models
from django.urls import reverse
# Create your models here.
class School(models.Model):
    Sname = models.CharField(max_length=100)
    Sprincipal = models.CharField(max_length=100)
    Slocation = models.CharField(max_length=100)
    def get_absolute_url(self):
        return reverse('SchoolDetail',kwargs={'pk':self.pk})
        
    def __str__(self):
        return self.Sname

class Student(models.Model):
    StudentName = models.CharField(max_length=100)
    StudentAge = models.IntegerField()
    Sname = models.ForeignKey(School,on_delete=models.CASCADE,related_name='students')

    def __str__(self):
        return self.StudentName