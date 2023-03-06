from django.db import models
from django.core.validators import MinLengthValidator, RegexValidator
from datetime import date

class Crust(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Size(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Sauce(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Cheese(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Pizza(models.Model):
    id = models.AutoField(primary_key=True)
    crust = models.ForeignKey(Crust, on_delete=models.CASCADE, default = 1)
    size = models.ForeignKey(Size, on_delete=models.CASCADE, default = 1)
    sauce = models.ForeignKey(Sauce, on_delete=models.CASCADE, default = 1)
    cheese = models.ForeignKey(Cheese, on_delete=models.CASCADE, default = 1)
    pepperoni = models.BooleanField(default=False)
    chicken = models.BooleanField(default=False)
    ham = models.BooleanField(default=False)
    pineapple = models.BooleanField(default=False)
    peppers = models.BooleanField(default=False)
    mushrooms = models.BooleanField(default=False)
    onions = models.BooleanField(default=False)
    olives = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)

class CustomerDetails(models.Model):
    COUNTY_CHOICES = (
        ("Antrim", "Antrim"),
        ("Armagh", "Armagh"),
        ("Carlow", "Carlow"),
        ("Cavan", "Cavan"),
        ("Clare", "Clare"),
        ("Cork", "Cork"),
        ("Derry", "Derry"),
        ("Donegal", "Donegal"),
        ("Down", "Down"),
        ("Dublin", "Dublin"),
        ("Fermanagh", "Fermanagh"),
        ("Galway", "Galway"),
        ("Kerry", "Kerry"),
        ("Kildare", "Kildare"),
        ("Kilkenny", "Kilkenny"),
        ("Laois", "Laois"),
        ("Leitrim", "Leitrim"),
        ("Limerick", "Limerick"),
        ("Longford", "Longford"),
        ("Louth", "Louth"),
        ("Mayo", "Mayo"),
        ("Meath", "Meath"),
        ("Monaghan", "Monaghan"),
        ("Offaly", "Offaly"),
        ("Roscommon", "Roscommon"),
        ("Sligo", "Sligo"),
        ("Tipperary", "Tipperary"),
        ("Tyrone", "Tyrone"),
        ("Waterford", "Waterford"),
        ("Westmeath", "Westmeath"),
        ("Wexford", "Wexford"),
        ("Wicklow", "Wicklow"))

    YEAR_CHOICES = ((str(y),y) for y in range(date.today().year, date.today().year + 15))
    MONTH_CHOICES = ((str(m),m) for m in range(1,13))

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    address1 = models.CharField("Address Line 1", max_length=50)
    address2 = models.CharField("Address Line 2", max_length=50, blank=True)
    city = models.CharField(max_length=50)
    county = models.CharField(max_length=20, choices=COUNTY_CHOICES)
    eircode = models.CharField(max_length=7,
        validators=[
            MinLengthValidator(7), # ensuring eircode is 7 characters long
            RegexValidator(r'[A-Z]\d{2}[A-Z]\d[A-Z]\d')
        ])
    cardnumber = models.CharField(max_length=19,
        validators=[
            MinLengthValidator(19), # ensuring card number is 19 digits long
            RegexValidator(r'^\d{4}-|\s\d{4}-|\s\d{4}-|\s\d{4}', message='Please enter in the format 1234 1234 1234 1234')
        ])
    expiration_month = models.CharField('Expiration Month',max_length=2, choices=MONTH_CHOICES)
    expiration_year = models.CharField('Expiration Year',max_length=4, choices=YEAR_CHOICES)
    cvv = models.CharField(max_length=3,
        validators=[
            MinLengthValidator(3),# ensuring cvv is 3 integers long
            RegexValidator(r'^\d{3}')
        ]
        )

    def __str__(self):
        return self.id
