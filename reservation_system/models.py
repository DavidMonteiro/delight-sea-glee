from datetime import date
from django.db import models
from django.contrib.auth.models import User

# model for tables here.
class Table(models.Model):
    number = models.IntegerField(unique=True, primary_key = True)
    capacity = models.IntegerField()

#Reservation number of guests has cannot be smaller than table/s or bigger than table/s capacity 
class Reservation(models.Model):
  datetime = models.DateTimeField()
  guests = models.PositiveIntegerField()
  table = models.ForeignKey(Table, on_delete=models.CASCADE)
  user = models.ForeignKey(
    User, on_delete=models.CASCADE, related_name="reservations"
  )

#model for reviews that costumer can leave
#class Review(models.Model):
#    rating_choises = [
#      (1, "1 Star"),
#      (2, "2 Star"),
#      (3, "3 Star"),
#      (4, "4 Star"),
#      (5, "5 Star")
#    ]
#    rating = models.IntegerField(default=3, choices=rating_choises)
#    review = models.SlugField(max_length=200, unique=True)
#    date_created = models.DateTimeField(auto_now_add=True)
#    reviewer = models.ForeignKey(
#      User, on_delete=models.CASCADE, related_name="reviews"
#    )