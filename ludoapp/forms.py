from django import forms
from .models import player,Battle,withdrawalaccount
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    phone = forms.CharField(max_length=122)
    password = forms.CharField(widget=forms.PasswordInput)
    
class playerForm(forms.ModelForm):

    class Meta:
        model = player
        fields = ['player_name', 'phone', 'player_email', 'password', 'confirm_password']

class kycForm(forms.ModelForm):
    class Meta:
        model = player
        fields = ['front_image', 'back_image']

class BattleForm(forms.ModelForm):
    class Meta:
        model = Battle
        fields = ['amount']

class PlayBattleForm(forms.Form):
    battle_id = forms.IntegerField(widget=forms.HiddenInput())


class WithdrawalAccountForm(forms.ModelForm):
    class Meta:
        model = withdrawalaccount
        fields = ['account_holder_name','upi_id', 'confirm_upi_id', 'amount']