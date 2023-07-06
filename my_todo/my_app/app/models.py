from django.db import models

class ToDo(models.Model):
    title = models.CharField(max_length=50, default='')
    note = models.CharField(max_length=200, default='')
    is_complete = models.BooleanField('Завершено', default= False)
    # created_at = models.DateField(default="")

    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'
    
    def __str__(self):
        return self.title