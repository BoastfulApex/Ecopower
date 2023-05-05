from django.db import models
import datetime

NEW, USED = (
    "new",
    "used",
)


class Brand(models.Model):
    name_uz = models.CharField(max_length=2000)
    name_en = models.CharField(max_length=2000)
    name_ru = models.CharField(max_length=2000)
    
    description_uz = models.TextField(max_length=5000)
    description_en = models.TextField(max_length=5000)
    description_ru = models.TextField(max_length=5000)

    image = models.FileField(null=True)
    

class Car(models.Model):
    
    USED_CHOICES = (
        (NEW, NEW),
        (USED, USED)
    )
    
    YEAR_CHOICES = [(year, year) for year in range(2000, datetime.date.today().year+1)]

    name_uz = models.CharField(max_length=2000)
    name_en = models.CharField(max_length=2000)
    name_ru = models.CharField(max_length=2000)
    
    description_uz = models.TextField(max_length=5000)
    description_en = models.TextField(max_length=5000)
    description_ru = models.TextField(max_length=5000)

    image1 = models.FileField(null=True)
    image2 = models.FileField(null=True)
    image3 = models.FileField(null=True)
    image4 = models.FileField(null=True)
    
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    
    used = models.CharField(max_length=100, choices=USED_CHOICES)
    
    produced = models.CharField(max_length=200, choices=YEAR_CHOICES)
    run = models.FloatField(default=0)

    top = models.BooleanField()
    

class Video(models.Model):
    description_uz = models.TextField(max_length=5000)
    description_en = models.TextField(max_length=5000)
    description_ru = models.TextField(max_length=5000)
    
    video = models.FileField(null=True)
    
    url = models.URLField(null=True)


class About(models.Model):
    name_uz = models.CharField(max_length=2000)
    name_en = models.CharField(max_length=2000)
    name_ru = models.CharField(max_length=2000)
    
    description_uz = models.TextField(max_length=15000)
    description_en = models.TextField(max_length=15000)
    description_ru = models.TextField(max_length=15000)

    image = models.FileField(null=True)
    
    
class Image(models.Model):
    description_uz = models.CharField(max_length=5000)
    description_en = models.CharField(max_length=5000)
    description_ru = models.CharField(max_length=5000)
    
    image = models.FileField(null=True)


class FAQ(models.Model):    
    question_uz = models.TextField(max_length=5000)
    question_en = models.TextField(max_length=5000)
    question_ru = models.TextField(max_length=5000)

    answer_uz = models.TextField(max_length=5000)
    answer_en = models.TextField(max_length=5000)
    answer_ru = models.TextField(max_length=5000)
