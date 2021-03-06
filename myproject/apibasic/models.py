from django.db import models

class Article(models.Model):
    title = models.CharField (max_length=50)
    author = models.CharField(max_length=50)
    email = models.EmailField(max_length=80)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title


