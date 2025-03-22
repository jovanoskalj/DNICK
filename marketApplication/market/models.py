from django.db import models
from django.contrib.auth.models import User


# За еден производ се чува неговото име, вид (храна, пијалок, пекара, козметика, хигиена),
# дали производот е домашен и неговиот код.
class Product(models.Model):
    TYPE_CHOICES = [
        ("F", "Food"),
        ("D", "Drink"),
        ("B", "Bakery"),
        ("C", "Cosmetic"),
        ("H", "Hygiene"),
    ]

    name = models.CharField(max_length=100)
    product_type = models.CharField(max_length=1, choices=TYPE_CHOICES)
    isHomeProduct = models.BooleanField(default=False)
    product_code = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"{self.name} - {self.get_product_type_display()} - {'Domestic' if self.isHomeProduct else 'Imported'} - {self.product_code}"


# За контакт информациите се чува улицата и бројот на којшто се наоѓа маркетот,
# телефонскиот број и емаил адресата.
class ContactInfo(models.Model):
    street = models.CharField(max_length=100)
    street_number = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    mail = models.EmailField()

    def __str__(self):
        return f"{self.street} {self.street_number}, {self.phone_number}, {self.mail}"


# Секој маркет се карактеризира со име, работен персонал, производи, контакт информации,
# број на маркети, датум на отварање, корисник којшто го додал, работно време од и работно време до.
class Market(models.Model):
    name = models.CharField(max_length=100)
    contact_info = models.ForeignKey(ContactInfo, on_delete=models.CASCADE)
    market_number = models.CharField(max_length=100)
    openingDate = models.DateField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    openingHour = models.TimeField()
    closingHour = models.TimeField()

    def __str__(self):
        return f"{self.name} (opens at {self.openingHour} - closes at {self.closingHour})"


# За секој вработен се чува неговото име, презиме, ЕМБГ, корисник кој што го
# додал, неговата плата. Еден вработен може да работи во само еден маркет.
class Employee(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    ssn = models.CharField(max_length=13, unique=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    market = models.ForeignKey(Market, on_delete=models.CASCADE, related_name="employees")
    salary = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} {self.surname}"


# За производите се знае во кои маркети се достапни како и достапната количина во секој од маркетите.
class MarketProduct(models.Model):
    market = models.ForeignKey(Market, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)


    def __str__(self):
        return f"{self.product.name} in {self.market.name} - {self.quantity} pcs"
