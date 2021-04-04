from django.db import models

# Create your models here.

class SubModel(models.Model):
	em=models.EmailField(max_length=30)
