from django.db import models
from django.urls import reverse
# Create your models here.
class Question(models.Model):
    content=models.TextField(max_length=10000)
    datetime=models.DateTimeField(auto_now=True)
    votes=models.IntegerField(default=0)
    def get_absolute_url(self):
        return reverse('detail',args=[str(self.pk)])

    def __str__(self):
        return self.content[:50]

class Answer(models.Model):
    content=models.TextField(max_length=10000)
    datetime=models.DateTimeField(auto_now=True)
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.content[:50] + ("..." if len(self.content) >50 else "")

class Comment(models.Model):
    content=models.TextField(max_length=10000)
    answer=models.ForeignKey(Answer,on_delete=models.CASCADE)
    def __str__(self):
        return self.content[:50]