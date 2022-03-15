from django.db import models

# Create your models here.

class food(models.Model):
    head = models.CharField(max_length=250)
    des = models.TextField()
    img = models.ImageField(upload_to='pics')

    def __str__(self):
        return self.head



