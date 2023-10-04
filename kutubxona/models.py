from django.db import models
from django.utils.text import slugify


class Author(models.Model):
    name=models.CharField(max_length=50)
    surname=models.CharField(max_length=50)
    birth_year=models.DateField(blank=True)

    class Meta:
        db_table ="auther"

    def __str__(self):
        return  f"{self.name} {self.surname}"


class Book(models.Model):
    title=models.CharField(max_length=100)
    author=models.ForeignKey(Author,on_delete=models.CASCADE,)
    genre=models.CharField(max_length=100)
    picture=models.ImageField(upload_to='images/',blank=True)
    body=models.TextField(blank=True)
    slug=models.CharField(max_length=100,blank=True,unique=True,null=True)

    class Meta:
        db_table ="books"

    def __str__(self):
        return  f"{self.title}"

    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         self.slug = slugify(self.title)
    #     super().save(*args, **kwargs)