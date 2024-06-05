# from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta

# Create your models here.

def validate_phone_length(value):
    if len(str(value)) != 10:
        raise ValidationError('Phone number must be 10 digits long.')


class player(models.Model):
    player_name = models.CharField(max_length=122)
    phone = models.BigIntegerField(validators=[validate_phone_length], primary_key=True)
    player_email = models.EmailField(max_length=122)
    password = models.CharField(max_length=122)
    confirm_password = models.CharField(max_length=122)
    front_image = models.ImageField(upload_to='images/',null=True)
    back_image = models.ImageField(upload_to='images/',null=True)
    wallet_balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    approved = models.BooleanField(default=False)
    # kyc_status = models.CharField(max_length=20, default='pending')

    class Meta:
            db_table='player'
            ordering = ['player_name']


class Battle(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    is_running = models.BooleanField(default=False)
    creator = models.ForeignKey(player, related_name='created_battles', on_delete=models.CASCADE,default=None)
    opponent = models.ForeignKey(player, related_name='joined_battles', null=True, blank=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=20, default='open')  # open, requested, accepted
    # room_code = models.CharField(max_length=10, null=True, blank=True)


    def __str__(self):
        return f'Battle for ₹{self.amount} - {"Running" if self.is_running else "Open"}'


class withdrawalaccount(models.Model):
    player = models.ForeignKey(player, on_delete=models.CASCADE)
    withdraw_at = models.DateTimeField(auto_now_add=True)
    account_holder_name = models.CharField(max_length=255)
    upi_id = models.CharField(max_length=255)
    confirm_upi_id = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.account_holder_name} - {self.upi_id}"


    def is_expired(self):
        return timezone.now() > self.created_at + timedelta(minutes=1)