from django.db import models
class Statue(models.Model):
    session_number=models.CharField(max_length=128)
    status_CHOICES=[('1','1'),('0','0')]
    status_in_shafafstu = models.CharField(max_length=1, choices=status_CHOICES)
    ordernumber=models.CharField(max_length=128)
    date=models.CharField(max_length=64)
    description=models.TextField()
    source=models.CharField(max_length=128)
    cost=models.CharField(max_length=128)
    ghaedi=models.CharField(max_length=128)
    point1=models.CharField(max_length=128)
    banafi=models.CharField(max_length=128)
    point2=models.CharField(max_length=128)
    gharibzade=models.CharField(max_length=128)
    point3=models.CharField(max_length=128)
    bibak=models.CharField(max_length=128)
    point4=models.CharField(max_length=128)
    behbahhani=models.CharField(max_length=128)
    point5=models.CharField(max_length=128)
    kazemi=models.CharField(max_length=128)
    point6=models.CharField(max_length=128)
    mahdaviyanpor=models.CharField(max_length=128)
    point7=models.CharField(max_length=128)

    class Meta():
        ordering = ['session_number']
        indexes = [models.Index(fields=["session_number"]),
        ]

    def __str__(self):
        return self.session_number
# Create your models here.
