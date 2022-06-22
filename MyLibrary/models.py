from django.db import models




class Book(models.Model):
    bookname = models.CharField(max_length=500)
    author = models.CharField(max_length=500)
    quantity = models.IntegerField(null=True)

    def __str__(self):
        return self.bookname
