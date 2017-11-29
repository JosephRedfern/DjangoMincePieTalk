from django.db import models
from django.db.models import Avg
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator

class Pie(models.Model):
    name = models.CharField(max_length=255)
    date_added = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    
    def get_average_rating(self):
        ratings =  Rating.objects.filter(pie=self)
        return ratings.aggregate(avg=Avg('pastry') + Avg('filling'))['avg']

    def __str__(self):
        return self.name
    
class Rating(models.Model):
    date_added = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User)
    pie = models.ForeignKey(Pie)
    pastry = models.DecimalField(validators=[MaxValueValidator(5)],
                                 max_digits=4, decimal_places=2)
    filling = models.DecimalField(validators=[MaxValueValidator(5)],
                                 max_digits=4, decimal_places=2)
    comments = models.TextField()
