from django.db import models

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=25)
    second_name = models.CharField(max_length=25)
    student_id = models.IntegerField()

    TEACHER = (
        ("golshan" , "Golshan") ,
        ("shahraki" , "Shahraki") ,
        ("somedude" , "Somedude") ,
        ("bruh" , "Bruh") ,
    )
    teacher = models.CharField(max_length=8 , choices=TEACHER)