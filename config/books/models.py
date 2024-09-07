from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length = 250,verbose_name="Название")

    author = models.CharField(max_length = 50,verbose_name="Автор")
    price = models.IntegerField(verbose_name="Цена")

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"
