from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.
class Personal_Information(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    profession = models.CharField(max_length=255)
    nationality = models.CharField(max_length=255)
    freelance = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=13)
    email = models.EmailField()
    github = models.CharField(max_length=255)
    langauges = models.CharField(max_length=255)
    cv = models.FileField(upload_to='documents/')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f"${self.first_name} - ${self.last_name} "


class Achievement(models.Model):
    years_of_experience = models.IntegerField(validators=[MinValueValidator(0)])
    completed_projects = models.IntegerField(validators=[MinValueValidator(0)])
    happy_customers = models.IntegerField(validators=[MinValueValidator(0)])
    awards = models.IntegerField(validators=[MinValueValidator(0)])
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)



class Skills(models.Model):
    name = models.CharField(max_length=255, unique=True)
    level = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)


class Experience(models.Model):
    year = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

class Education(models.Model):
    degree = models.CharField(max_length=255)
    year = models.CharField(max_length=255)
    university = models.CharField(max_length=255)
    field_study = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

class Portfolio(models.Model):
    title = models.CharField(max_length=255)
    langauge = models.CharField(max_length=255)
    link = models.URLField()
    client = models.CharField(max_length=255)
    project_type = models.CharField(max_length=255)
    image = models.ImageField(upload_to="portfolio")
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)



class PortfolioGallery(models.Model):
    portfolio = models.ForeignKey(
        Portfolio, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='gallery')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.portfolio.title

    class Meta:
        verbose_name = 'portfoliogallery'
        verbose_name_plural = 'portfolio gallery'


class Contact(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
   