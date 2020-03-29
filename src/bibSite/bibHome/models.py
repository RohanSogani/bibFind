from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Bib(models.Model):
    title = models.CharField(max_length = 1000)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    bib = models.TextField()
    date_searched = models.DateTimeField(auto_now_add = True)

    # To make the object descriptive in the shell
    def __str__(self):
        return self.title
