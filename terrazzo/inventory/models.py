from django.db import models

# Create your models here.

class Category(models.Model):

    snipe_id = models.IntegerField(default=0)
    name = models.CharField(max_length=128)
    category_type = models.CharField(max_length=128)
    item_count = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Categories"
    
class CategoryField(models.Model):

    name = models.CharField(max_length=128)
    display = models.BooleanField(default=False)
    category = models.ForeignKey(Category, related_name='fields', on_delete=models.CASCADE)

    def __str__(self):
        return self.name