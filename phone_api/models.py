from django.db import models


# Create your models here.
class PhonesLookedUp(models.Model):
    phone_number = models.CharField(max_length=11)
    operator = models.CharField(max_length=200)
    region = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.phone_number
