from django.db import models

class CV (models.Model):

    class education_choices(models.TextChoices):
        Primary =  "Primary"
        Secondary = "Secondary"
        Higher =  "Higher"


    First_Name = models.CharField(max_length=20)
    Last_Name = models.CharField(max_length=30)
    Pfp = models.ImageField(upload_to='ttt',blank=True)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=11)
    date_of_birth = models.CharField(max_length=11,default="")
    bio = models.TextField(blank=True)
    education = models.CharField(max_length=10,choices=education_choices.choices,default=education_choices.Secondary)
    school = models.CharField(max_length=50,blank=True)
    experience = models.TextField(blank=True)
    skills = models.TextField(blank=True)

    def __str__(self):
        return self.First_Name