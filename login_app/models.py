from django.db import models
from users.models import User
from django.contrib.auth import get_user_model

class profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.PROTECT)
    phone = models.CharField(max_length=50,default='')
    address = models.CharField(max_length=200,default='')
    zip_code = models.IntegerField(default=0)
    country = models.CharField(max_length=100,default='')
    card_holder = models.CharField(max_length=100,default='')
    card_number = models.IntegerField(default=1234123412341234)
    cvc = models.IntegerField(default=123)
    expiration_month = models.CharField(max_length=100,default='DECEMBER')
    expiration_year = models.IntegerField(default=2021)
    picture = models.ImageField(upload_to='profile',null=True)
    password_key = models.CharField(max_length=50,default='')

    def __str__(self):
        return ('Profile belonging to {}'.format(self.user))

class Payment_keys(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    payment_method_key = models.CharField(max_length=150,default='')
    customer_Id = models.CharField(max_length=150,default='')
    timestamp = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.user.username