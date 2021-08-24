from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    # slug = models.SlugField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    description = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return f'127.0.0.1:8000/{self.slug}/'
    
