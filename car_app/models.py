from django.contrib.auth import get_user_model

from django.db import models

from django.urls import reverse

class Car(models.Model):
   
    name_of_car = models.CharField(max_length=64)
   
    body = models.TextField()
   
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

   
    created_at =models.DateTimeField(auto_now_add=True)
   
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
   
        return self.name_of_car
   
    def get_absolute_url(self):
   
        return reverse('cars_list')  