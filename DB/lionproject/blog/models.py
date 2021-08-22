from django.db import models

# Create your models here.
# Class의 이름은 만들 테이블(blog)의 이름과 같아야함
class Blog(models.Model):
    title = models.CharField(max_length=200)
    writer = models.CharField( max_length=100)
    body =  models.TextField()
    pub_date = models.DateTimeField()

    def __str__(self):
        return self.title

    def summary(self) :
        return self.body[:100]