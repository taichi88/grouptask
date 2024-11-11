from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


# Create your models here.

class Car(models.Model):
    make = models.CharField(max_length=100)
    model = models.TextField()
    year_model = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1960),
            MaxValueValidator(2024)
        ]
    )
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    user = models.ForeignKey(User, related_name="cars",on_delete=models.CASCADE)
    slug = models.SlugField(null=False, unique=True)
    class Meta:
        verbose_name = "Car"
        verbose_name_plural = "Cars"
        ordering = ["-make"]

    def __str__(self):
        return self.make

    def save(self, *args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.make)
        return super().save(*args,**kwargs)