from django.db import models

# Create your models here.

class Skill(models.Model):

    name=models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.name

class Job(models.Model):

        EXPERIENCE_CHOICES = [
        ('fresher', 'Fresher'),
        ('1-2 years', '1-2 Years'),
        ('3-5 years', '3-5 Years'),
        ('5+ years', '5+ Years'),
        ]

        title = models.CharField(max_length=150)

        company_name = models.CharField(max_length=150)

        description = models.TextField()

        required_skills = models.ManyToManyField(Skill,
        related_name='jobs'
        )

        experience_level = models.CharField(
        max_length=20,
        choices= EXPERIENCE_CHOICES
        )

        location = models.CharField(max_length=150)

        is_active = models.BooleanField(default=True)

        created_at = models.DateTimeField(auto_now_add=True)

        def __str__(self):
            return self.title