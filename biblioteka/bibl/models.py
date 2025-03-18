from django.db import models
from django.contrib.auth.models import User

class Translator(models.Model):
    name = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    birth_date = models.DateField()

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    birth_date = models.DateField()

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    # authors = models.ManyToManyField(Author)
    # genres = models.ManyToManyField(Genre)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)
    issue_date = models.DateField()
    num_pages = models.IntegerField()
    book_cover = models.ImageField(upload_to='book_cover/', null=True, blank=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class BookAuthors(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

class BookGenres(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

class BookTranslators(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    translator = models.ForeignKey(Translator, on_delete=models.CASCADE)

class Rating(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    rating = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.first_name + ", " + str(self.rating)