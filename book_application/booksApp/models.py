from django.db import models
from django.contrib.auth.models import User


# За секоја издавачка
# куќа се знае име, земја и град во кој се наоѓа главната канцеларија и вебсајт.
class PublishingHouse (models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    website = models.CharField(max_length=300)

    def __str__(self):
        return f"{self.name} {self.country}"

# Секоја книга се карактеризира со наслов, слика, ISBN,
# година на издавање, издавачка куќа, број на страни, димензии на книгата,
# тип на корица на книга (мека, тврда),
# категорија (романса, трилер, биографија, класика, драма, историја) и цена.
class Book (models.Model):
    COVER_TYPES = [
        ("H", "Hard"),
        ("S", "Soft"),
    ]
    CATEGORY_TYPES  = [
        ("R","Romance"),
        ("T","Thriller"),
        ("B","Biography"),
        ("C","Classic"),
        ("D","Drama"),
        ("H","History"),
    ]
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='books_photo/', blank=True, null=True)
    ISBN = models.CharField(max_length=100)
    year_of_publishing = models.DateField()
    pages = models.IntegerField()
    dimension = models.CharField(max_length=50)
    cover_type = models.CharField(max_length=1, choices=COVER_TYPES)
    category = models.CharField(max_length=1, choices=CATEGORY_TYPES)
    publishing_house = models.ForeignKey(PublishingHouse, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} {self.publishing_house}"










