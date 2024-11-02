from django.db import models

class Order(models.Model):
    food_name = models.CharField(max_length=100)
    table_number = models.CharField(max_length=10)
    person_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.food_name} ordered by {self.person_name} at table {self.table_number}"
