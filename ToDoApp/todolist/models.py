from django.db import models


class ToDo(models.Model):
    title = models.CharField('Задание', max_length= 100)
    is_complete = models.BooleanField('Завершено', default= False)

    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'

    def __str__(self):
        return self.title