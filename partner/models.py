from django.db import models

class addshop(models.Model):
    shop_name =  models.CharField(max_length=100)
    shop_img = models.ImageField(upload_to="addshop")
    shop_contact = models.CharField(max_length=12)
    shop_address = models.CharField(max_length=200)
    