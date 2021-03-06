from django.db import models

class Item(models.Model):

    def __str__(self):
        return self.item_name

    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=1000, default="https://i.pinimg.com/originals/b6/9d/53/b69d53168ccb8e5daab6d5d460b773d8.jpg")
 