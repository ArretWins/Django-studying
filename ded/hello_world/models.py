from django.db import models

class workers(models.Model):
    age = models.CharField(max_length = 15, blank=False)
    surname = models.CharField(max_length= 20, blank=False)
    salary = models.IntegerField(default=0)
    
    # def __str__(self):
    #     return f'{self.surname} {self.age} - {self.salary}'