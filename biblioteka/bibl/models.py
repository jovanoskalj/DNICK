from django.db import models
from django.contrib.auth.models import User

class Genre(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Translator(models.Model):
    name = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    birth_date = models.DateField()

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publish_date = models.DateField()
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)
    page_count = models.PositiveIntegerField()
    cover_image = models.ImageField(upload_to='covers/', null=True, blank=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def average_rating(self):
        ratings = self.ratings.all()
        if ratings.exists():
            return sum(r.rating for r in ratings) / ratings.count()
        return None

class BookGenre(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='book_genres')
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.book.title} - {self.genre.name}"

class BookTranslator(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='book_translators')
    translator = models.ForeignKey(Translator, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.book.title} - {self.translator.name}"

class Rating(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.book.title} - {self.rating} by {self.user.username}"
