from django.db import models

# Create your models here.
class bank_dtl(models.Model):
    bank_name=models.CharField(max_length=28)
    bank_location=models.CharField(max_length=39)
    opp_amount=models.IntegerField()
    holder_name=models.CharField(max_length=23)
    holder_location=models.CharField(max_length=37)
    def __str__(self):
        return bank_dtl