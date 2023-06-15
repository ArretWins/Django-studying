from django.db import models
import datetime
from django.utils import timezone

class Article(models.Model):
    title = models.CharField('Название статьи', max_length=50)
    text = models.TextField('Содержание статьи')
    date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.title
    
    def was_published_recently(self):
        return self.date >= (timezone.now() - datetime.timedelta(days= 7)) #была ли запись меньше 7 дней(опубликована недавно)



class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author_name = models.CharField('Имя автора', max_length=50)
    comment_text = models.CharField('Текст комментария', max_length=200)
    
    def __str__(self):
        return self.comment_text