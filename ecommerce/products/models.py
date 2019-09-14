from django.db import models

# Create your models here.


class ProductModel(models.Model):
    product_name        = models.CharField(max_length=65)
    detail              = models.TextField()
    category            = models.CharField(max_length=40)
    quantity            = models.IntegerField(blank=True)
    price               = models.IntegerField(blank=True)
    image               = models.ImageField(upload_to='upload/')

    def __str__(self):
        return "{}. {}".format(self.id, self.product_name)

    class Meta:
        ordering = ['-id']
    