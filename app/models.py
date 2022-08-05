from django.db import models

# Create your models here.
class Movies(models.Model):
    name=models.CharField(max_length=250)
    year=models.DateField()
    des=models.TextField()
    img=models.ImageField(upload_to='pics')
    def __str__(self):
        return self.name