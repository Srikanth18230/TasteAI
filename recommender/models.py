from django.db import models

class Cart(models.Model):
    food_name = models.CharField(max_length=100)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    recommended_food = models.CharField(max_length=100, null=True, blank=True)
    order_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.food_name
