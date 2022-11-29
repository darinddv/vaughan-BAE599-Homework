from django.db import models

# Create your models here.

class Field(models.Model):
    field_name = models.CharField(max_length=100)
    poly_coord1 = models.CharField(max_length=100)
    poly_coord2 = models.CharField(max_length=100)
    poly_coord3 = models.CharField(max_length=100)
    poly_coord4 = models.CharField(max_length=100)
    def __str__(self):
        return self.field_name