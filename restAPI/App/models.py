from django.db import models

# Create your models here.
class BookModel(models.Model):

    bookname = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return self.bookname
