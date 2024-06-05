from django.shortcuts import render,redirect,get_object_or_404
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.http import request
from django.views.generic import TemplateView
from django.conf import settings
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from .models import player,Battle,withdrawalaccount
from django.contrib.auth.decorators import login_required
from .forms import playerForm, LoginForm,kycForm,BattleForm,PlayBattleForm ,WithdrawalAccountForm #,playForm
# from django.core.management.base import BaseCommand
# from celery import shared_task
# from celery.schedules import crontab
from django.utils import timezone
from datetime import timedelta
import urllib.parse




# Import your payment gateway API client (replace with your actual payment gateway library)
# from your_payment_gateway_library import PaymentGatewayClient

# class AddCashView(TemplateView):
#     template_name = 'add_cash.html'

#     def get(self, request, *args, **kwargs):
#         context = {
#             'amount': 0  # Initial amount, you can set this dynamically based on user input
#         }
#         return render(request, self.template_name, context)

#     def post(self, request, *args, **kwargs):
#         amount = request.POST.get('amount')

#         # Initialize your payment gateway client with your credentials
#         gateway_client = PaymentGatewayClient(
#             api_key=settings.PAYMENT_GATEWAY_API_KEY,
#             secret=settings.PAYMENT_GATEWAY_SECRET_KEY
#         )

#         # Example: Charge the user
#         payment_response = gateway_client.charge(amount)

#         # Check if payment was successful
#         if payment_response.success:
#             # Perform actions here like updating the user's wallet, logging the transaction, etc.
#             return redirect(reverse('ludoapp:wallet'))  # Redirect to wallet page after successful payment
#         else:
#             # Handle payment failure scenario
#             context = {
#                 'error_message': payment_response.error_message,
#                 'amount': amount
#             }
#             return render(request, self.template_name, context)




# class WithdrawCashView(TemplateView):
#     template_name = 'withdraw_cash.html'

#     def get(self, request, *args, **kwargs):
#         context = {
#             'amount': 0  # Initial amount, you can set this dynamically based on user input
#         }
#         return render(request, self.template_name, context)

#     def post(self, request, *args, **kwargs):
#         amount = request.POST.get('amount')

#         # Initialize your payment gateway client with your credentials
#         gateway_client = PaymentGatewayClient(
#             api_key=settings.PAYMENT_GATEWAY_API_KEY,
#             secret=settings.PAYMENT_GATEWAY_SECRET_KEY
#         )

#         # Example: Process withdrawal
#         withdrawal_response = gateway_client.withdraw(amount)

#         # Check if withdrawal was successful
#         if withdrawal_response.success:
#             # Perform actions here like updating the user's wallet, logging the transaction, etc.
#             return redirect(reverse('ludoapp:wallet'))  # Redirect to wallet page after successful withdrawal
#         else:
#             # Handle withdrawal failure scenario
#             context = {
#                 'error_message': withdrawal_response.error_message,
#                 'amount': amount
#             }
#             return render(request, self.template_name, context)


# class addmoney(TemplateView):
#     template_name = 'addmoney.html'

#     def get(self, request, *args, **kwargs):
#         return render(request, self.template_name)

#     def post(self, request, *args, **kwargs):
#         amount = request.POST.get('amount')

#         # Perform validation on amount (ensure it's a positive number)
#         try:
#             amount = float(amount)
#             if amount <= 0:
#                 raise ValueError("Amount must be positive")
#         except ValueError as e:
#             messages.error(request, str(e))
#             return redirect(reverse('ludoapp:addmoney'))

#         # Update user's wallet balance (assuming you have a Player model)
#         player = Player.objects.get(user=request.user)
#         player.wallet_balance += amount
#         player.save()

#         messages.success(request, f"Successfully added ${amount} to your wallet.")
#         return redirect(reverse('ludoapp:wallet'))














# Create your views here.
def refer(request):
    refer_code = '861335'  # Replace with your actual refer code
    context = {
        'refer_code': refer_code,
    }
    return render(request, 'refer.html', context)


from .utils import WhatsappRedirect
# Share via WhatsApp view
def share_whatsapp(request):
    refer_code = '861335'  # Replace with your actual refer code
    text = urllib.parse.quote(f"Use my refer code {refer_code} to join RK Ludo and earn rewards!")
    return WhatsappRedirect(f"whatsapp://send?text={text}")
    # return HttpResponseRedirect(f"whatsapp://send?text={text}")

# Share via Telegram view
def share_telegram(request):
    refer_code = '861335'  # Replace with your actual refer code
    text = urllib.parse.quote(f"Use my refer code {refer_code} to join RK Ludo and earn rewards!")
    return HttpResponseRedirect(f"https://telegram.me/share/url?url={text}")

# Copy refer code view
def copy_refer_code(request):
    refer_code = '861335'  # Replace with your actual refer code
    return render(request, 'copy_refer_code.html', {'refer_code': refer_code})

def battle_landing(request):
    return render(request, 'battle_landing.html')


# def create_battle(request):
    # if request.method == 'POST':
    #     form = BattleForm(request.POST)
    #     if form.is_valid():
    #         battle = form.save(commit=False)
    #         battle.save()
    #         return redirect('ludoapp:battle')  # Redirect to the landing page after creating the battle
    #     else:
    #         print("Form is not valid")
    #         print(form.errors)
    # else:
    #     form = BattleForm()

    # # battles = Battle.objects.filter(is_running=False)
    # return render(request, 'battle.html', {'form': form}) #, 'battles': battles})

# def landing(request):
#     # Delete expired battles
#     Battle.objects.filter(created_at__lt=timezone.now() - timedelta(minutes=1)).delete()

#     form = BattleForm()
#     battles = Battle.objects.filter(opponent__isnull=True)
#     return render(request, 'landing.html', {'form': form, 'battles': battles})

# @login_required
# def play_battle(request, battle_id):
#     battle = get_object_or_404(Battle, id=battle_id)
#     if not battle.opponent:
#         player = get_object_or_404(player, user=request.user)
#         battle.opponent = player
#         battle.save()
#         return redirect('accept_or_abort_request', battle_id=battle.id)
#     return redirect('battle_landing')

# @login_required
# def accept_or_abort_request(request, battle_id):
#     battle = get_object_or_404(Battle, id=battle_id)
#     if request.method == 'POST':
#         if 'accept' in request.POST:
#             battle.is_running = True
#             battle.room_code = request.POST.get('room_code')
#             battle.save()
#             return redirect('battle_landing')
#         elif 'abort' in request.POST:
#             battle.opponent = None
#             battle.save()
#             return redirect('battle_landing')
#     return render(request, 'battle/accept_or_abort.html', {'battle': battle})
# def approve_player(request, phone):
#     player = get_object_or_404(Player, id=phone)
#     if player.kyc_status != 'completed':
#         player.kyc_status = 'completed'
#         player.save()
#         messages.success(request, f'Player {player.phone} approved successfully.')
#     return redirect('ludoappp:playerdetail')  # Redirect to the list of players

# def delete_player(request, phone):
#     player = get_object_or_404(Player, id=phone)
#     if player.front_image:
#         player.front_image.delete()
#     if player.back_image:
#         player.back_image.delete()
#     player.delete()
#     player.kyc_status = 'completed'
#     messages.success(request, f'Player {player.phone} deleted successfully.')
#     return redirect('ludoapp:playerdetail')  # Redirect to the list of players

# import random

# def generate_otp():
#     return random.randint(100000, 999999)

# generate_otp()


# from django.shortcuts import render, redirect
# from django.http import JsonResponse
# # from .models import OTP
# # from .utils import generate_otp
def send_otp(request):
#     if request.method == 'POST':
#         phone_number = request.POST.get('phone_number')
#         otp = generate_otp()
#         # Save OTP to the database
#         OTP.objects.create(phone_number=phone_number, otp=otp)
#         # Mock sending OTP
#         print(f"Sending OTP {otp} to {phone_number}")
#         return JsonResponse({'message': 'OTP sent successfully'})
    return render(request, 'send_otp.html')

def verify_otp(request):
#     if request.method == 'POST':
#         phone_number = request.POST.get('phone_number')
#         otp = request.POST.get('otp')
#         otp_entry = OTP.objects.filter(phone_number=phone_number, otp=otp).first()
#         if otp_entry and otp_entry.is_valid():
#             otp_entry.is_used = True
#             otp_entry.save()
#             return JsonResponse({'message': 'OTP verified successfully'})
#         return JsonResponse({'message': 'Invalid OTP or OTP expired'})
    return render(request, 'verify_otp.html')



def index(request):
    return render(request,'index.html')


def policy(request):
    return render(request,'policy.html')

def refer(request):
    return render(request,'refer.html')

def support1(request):
    return render(request,'support1.html')

def addmoney(request):
    phone = request.session.get('phone')
    if request.method == 'POST':
        player_instance = get_object_or_404(player, phone=phone)
        # user = request.phone
        amount = request.POST['amount']
        print(amount)
        if not amount.isdigit():
            messages.error(request, 'Please enter a valid amount.')
            return redirect('ludoapp:addmoney')
        # user_wallet = wallet.objects.get(user=user)
        player_instance.wallet_balance=player_instance.wallet_balance+int(amount)
        player_instance.save()
        print(player_instance.wallet_balance)
        messages.success(request, f'{amount} has been added to your wallet.')
        return redirect('ludoapp:wallet')
    else:
        return render(request, 'addmoney.html')


    # phone = request.session.get('phone')
    # template_name = 'addmoney.html'

    # def get(self, request, *args, **kwargs):
    #     return render(request, self.template_name)

    # def post(self, request, *args, **kwargs):
    #     amount = request.POST.get('amount')

    #     # Perform validation on amount (ensure it's a positive number)
    #     try:
    #         amount = float(amount)
    #         if amount <= 0:
    #             raise ValueError("Amount must be positive")
    #     except ValueError as e:
    #         messages.error(request, str(e))
    #         return redirect(reverse('ludoapp:addmoney'))

    #     # Update user's wallet balance (assuming you have a Player model)
    #     player = Player.objects.get(phone=request.phone)
    #     player.wallet_balance += amount
    #     player.save()

    #     messages.success(request, f"Successfully added ${amount} to your wallet.")
    #     return redirect(reverse('ludoapp:wallet'))
    # return render(request,'addmoney.html')

def withdrawal(request):
    return render(request,'withdrawal.html')


def withdrawalaccount(request):
    if request.method == 'POST':
        phone = request.session.get('phone')
        player_instance, created = player.objects.get_or_create(phone=phone)
        form = WithdrawalAccountForm(request.POST)
        if form.is_valid():
            # user = form.save(commit=False)
            user = form.save(commit=False)
            user.player = player_instance
            # user = player.objects.get(phone=phone)
            # user.save()
            # user1 = withdrawalaccount.objects.get()
            user.account_holder_name = form.cleaned_data['account_holder_name']
            user.upi_id = form.cleaned_data['upi_id']
            user.confirm_upi_id = form.cleaned_data['confirm_upi_id']
            user.amount = form.cleaned_data['amount']
            if user.upi_id!= user.confirm_upi_id:
                form.add_error('confirm_upi_id', 'UPI ID and Confirm UPI ID do not match')
                return render(request, 'withdrawalaccount.html', {'form': form})
                withdrawalaccount.player.delete()

            if user.amount > player_instance.wallet_balance:
                form.add_error('amount', 'Insufficient balance')
                return render(request, 'withdrawalaccount.html', {'form': form})
            player_instance.wallet_balance=player_instance.wallet_balance - user.amount
            player_instance.save()
            user.save()
            return redirect('ludoapp:wallet')
        else:
            print(form.errors)
    else:
        form = WithdrawalAccountForm()
    return render(request, 'withdrawalaccount.html', {'form': form})

    # return render(request,'withdrawalaccount.html')


# def play_battle_view(request):
#     if request.method == 'POST':
#         # phone = request.session.get('phone')
#         # player_instance = get_object_or_404(player, phone=phone)
#         # battle = get_object_or_404(Battle, player=player_instance)
#         # battle_id = request.POST.get('battle_id')
#         if phone:  # Ensure phone is not None
#             player_instance = get_object_or_404(player, phone=phone)
#             battle = get_object_or_404(Battle, player=player_instance)
#             battle.is_running = True
#         # battle_id = request.GET.get('id')
#         # battle = get_object_or_404(Battle, id=battle_id)
#         # battle.is_running = True
#             battle.save()
#             return render(request, 'ludoapp:battle.html', {'message': 'Game started!'})
#         else:
#             return render(request, 'ludoapp:battle.html', {'message': 'Phone number not found in session.'})
#     else:
#         return render(request, 'ludoapp:battle.html')


    #             return JsonResponse({'success': True})
    #     else:
    #         return render(request, 'ludoapp:battle.html')
    # else:
    #     return render(request, 'ludoapp:battle.html')
        # return JsonResponse({'error': 'Invalid request'}, status=400)

def accept_battle_view(request):
    if request.method == 'POST':
        battle_id = request.GET.get('id')
        battle = get_object_or_404(Battle, id=battle_id)
        battle.is_running = True
        battle.save()
        return JsonResponse({'success': True})
    return JsonResponse({'error': 'Invalid request'}, status=400)

def delete_battle_view(request):
    if request.method == 'POST':
        battle_id = request.GET.get('id')
        battle = get_object_or_404(Battle, id=battle_id)
        battle.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'error': 'Invalid request'}, status=400)


# def playbattle(request):
#     if request.method == 'POST':
#         battle_id = request.POST.get('phone')
#         battle = get_object_or_404(Battle, phone=phone)
#         phone = request.session.get('phone')
#         player_instance = get_object_or_404(player, phone=phone)

#         if battle.creator == player_instance:
#             action = request.POST.get('action')
#             if action == 'accept':
#                 battle.is_running = True
#                 battle.save()
#             elif action == 'delete':
#                 battle.delete()
#         else:
#             battle.opponent = player_instance
#             battle.is_running = True
#             battle.save()
        
        # return redirect('ludoapp:battle')

    # return redirect('ludoapp:battle')  # Ensure to redirect on non-POST request


# def play_battle(request):
#     if request.method == 'POST':
#         form = PlayBattleForm(request.POST)
#         if form.is_valid():
#             phone = request.session.get('phone')
            
#             battle_id = form.cleaned_data['battle_id']
#             battle = get_object_or_404(Battle, id=battle_id)
#             print(battle.creator)
#             creator_phone = battle.creator
#             print(f"Creator phone: {creator_phone}")
#             # opponent_phone = battle.opponent.phone
            
            
#             opponent_phone = battle.opponent if battle.opponent else None
            
#             if phone == creator_phone:
#                 print(creator_phone)
#                 print(phone)
#                 print("first method is chalu")
#                 return redirect(reverse('ludoapp:battle'))  # Creators cannot join their own battles

#             else:
#                 if not battle.opponent:
#                     print(opponent_phone)
#                     # opponent_phone = get_object_or_404(player, phone=phone)
#                     battle.opponent = phone
#                     battle.status = 'requested'
#                     battle.save()
#                     print("second method is chalu")
#                     return redirect(reverse('ludoapp:battle'))
#                 else:
#                     return redirect(reverse('ludoapp:battle'))
#             # return redirect(reverse('ludoapp:battle'))
#         else:
#             return redirect(reverse('ludoapp:battle')) #, {'form': form})  # Redirect to the battle view
#     return redirect(reverse('ludoapp:battle'))
    # return render(request, 'ludoapp:battle', {'form': PlayBattleForm()})



# def play_battle(request):
#     if request.method == 'POST':
#         form = PlayBattleForm(request.POST)
#         if form.is_valid():
#             phone = request.session.get('phone')
#             print(f"Session phone: {phone}")
            
#             battle_id = form.cleaned_data['battle_id']
#             battle = get_object_or_404(Battle, id=battle_id)
#             creator_phone = battle.creator
#             print(f"Creator phone: {creator_phone}")
#             # Check if the player is the creator
#             if phone == creator_phone:
#                 print("The user is the creator")
#                 print(phone)
#                 print(creator_phone)
#                 print("creator h ji")
#                 # Creators cannot join their own battles
#                 return redirect(reverse('ludoapp:battle'))
#             else:
#                 if not battle.opponent:
#                     opponent = get_object_or_404(player, phone=phone)
#                     battle.opponent = opponent
#                     battle.status = 'requested'
#                     battle.save()
#                     print(phone)
#                     print(opponent)
#                     print("The user is the opponent")
#                     print("opponent h ji")
#                     return redirect(reverse('ludoapp:battle'))
#         return render(request, 'ludoapp:battle', {'form': form})
#     return render(request, 'ludoapp:battle', {'form': PlayBattleForm()})


def accept_battle(request, battle_id):
    battle = get_object_or_404(Battle, id=battle_id)
    phone = request.session.get('phone')

    if battle.opponent and battle.opponent.phone == phone:
        if request.method == 'POST':
            action = request.POST.get('action')
            if action == 'accept':
                battle.status = 'accepted'
            elif action == 'decline':
                battle.opponent = None
                battle.status = 'open'
            battle.save()

    return redirect(reverse('ludoapp:battle'))


# def battle_view(request):
#     bdetail = Battle.objects.all()
#     return render(request, 'ludoapp/battle.html', {'bdetail': bdetail})
    
def viewbattle(request):
    return render(request,'viewbattle.html')

def setbattle(request):
    return render(request,'setbattle.html')


def play_battle(request, battle_id):
    print(battle_id)
    battle = get_object_or_404(Battle, id=battle_id)
    print(battle)

    if request.method == 'POST':
        if battle.creator == request.user:
            print(request.user)
            print(battle.creator)
            # Creator cannot join their own battle
            return redirect('ludoapp:battle', battle_id=battle.id)

        if battle.status == 'open':
            battle.opponent = request.user
            battle.status = 'requested'
            battle.save()

    return redirect('ludoapp:battle', battle_id=battle.id)

def battle(request):
    # phone = request.session.get('phone')
    if request.method == 'POST':
        form = BattleForm(request.POST)
        if form.is_valid():
            phone = request.session.get('phone')
            if phone:  # Ensure phone is not None
                player_instance = get_object_or_404(player, phone=phone)
                battle = form.save(commit=False)
                battle.creator = player_instance
                battle.save()
                return redirect('ludoapp:battle')  # Redirect to the landing page after creating the battle
            else:
                # Handle case where phone is not found in session
                form.add_error(None, "Phone number not found in session.")
        else:
            print("Form is not valid")
            print(form.errors)
    else:
        cutoff_time = timezone.now() - timedelta(minutes=5)
        bdetail = Battle.objects.filter(is_running=False, created_at__lt=cutoff_time)
        bdetail.delete()  # Delete older battles
        
        bdetail = Battle.objects.filter(is_running=False)
        return render(request,'battle.html',{'bdetail': bdetail})
        # form = BattleForm()

    # battles = Battle.objects.filter(is_running=False)
    if request.method == 'GET':
        battle_id = request.GET.get('battle_id')  # Get battle id from URL parameter
        try:
            battle = Battle.objects.get(pk=battle_id)
        except Battle.DoesNotExist:
            return redirect('battle')  # Redirect back if battle doesn't exist

        # Check if player is the creator
        if battle.creator == request.session.get('phone'):
        # Show Accept and Delete buttons for creator
            battle.button_options = ['Accept', 'Delete']
        else:
        # Check if battle is already requested
            if battle.opponent:
            # Show Requested button if already requested
                battle.button_options = ['Requested']
            else:
            # Save player phone as opponent and update status
                battle.opponent = request.session.get('phone')
                battle.status = 'requested'
                battle.save()
                # Show Requested button after joining
                battle.button_options = ['Requested']

        return render(request, 'battle.html', {'battles': battles, 'battle': battle})

    return render(request, 'battle.html', {'form': form}) #, 'battles': battles})
    # bdetail = Battle.objects.filter(is_running=False)
    # return render(request,'battle.html',{'bdetail': bdetail})

# class Command(BaseCommand):
#     help = 'Delete battles that are older than one minute'

#     def handle(self, *args, **kwargs):
#         one_minute_ago = timezone.now() - timedelta(minutes=1)
#         expired_battles = Battle.objects.filter(created_at__lt=one_minute_ago, is_running=False)
#         expired_battles.delete()
#         self.stdout.write(self.style.SUCCESS(f'Deleted {expired_battles.count()} expired battles'))

# @shared_task
# def delete_expired_battles():
#     one_minute_ago = timezone.now() - timedelta(minutes=1)
#     expired_battles = Battle.objects.filter(created_at__lt=one_minute_ago, is_running=False)
#     expired_battles.delete()


# app.conf.beat_schedule = {
#     'delete-expired-battles-every-minute': {
#         'task': 'ludoapp.tasks.delete_expired_battles',
#         'schedule': crontab(minute='*'),
#     },
# }


def indexlogin(request):
    return render(request,'indexlogin.html')

# def landing(request):
#     # player_phone=phone
#     return render(request,'landing.html') #,{'player_phone':player_phone})


def landing(request):
    phone = request.session.get('phone')
    print(phone)
    return render(request, 'landing.html', {'phone': phone})


# def demo(request):
#     # pdetail = player.objects.get(phone=player_phone)
#     # return render(request, 'demo.html', {'pdetail': pdetail,'player_phone':player_phone})
#     return render(request,'demo.html')

def approve_player(request, phone):
    player_instance = get_object_or_404(player, phone=phone)
    if request.method == 'POST':
        # player = get_object_or_404(player, phone=phone)
        player_instance.approved = True
        player_instance.save()
        return redirect('ludoapp:playerdetail') #, phone=phone)
    return render(request, 'playerdetail.html', {'pdetail': player.objects.all()})
    # else:

    #     return render(request,'playerdetail.html')  

def delete_player(request, phone):
    player_instance=get_object_or_404(player, phone=phone)
    if request.method == 'POST':
        # player =player.objects.get(phone=phone) # get_object_or_404(player, phone=phone)
        
        if player_instance.front_image:
            player_instance.front_image.delete(save=False)  # Delete the front image file
        if player_instance.back_image:
            player_instance.back_image.delete(save=False)   # Delete the back image file
        
        player_instance.save()
        
        return redirect('ludoapp:playerdetail') #, phone=phone)  # Redirect to the player detail view/page
    # else:
    #     return render(request, "ludoapp:playerdetail.html")
    

def demo(request):
    phone = request.session.get('phone')
    print(phone)
    return render(request, 'demo.html', {'phone': phone})


def playerdetail(request):
    pdetail = player.objects.all()
    return render(request, 'playerdetail.html', {'pdetail': pdetail})

# def kyc(request):
#     # user = get_object_or_404(player, phone=player_phone)
#     if request.method == 'POST':
#         form = kycForm(request.POST, request.FILES)
#         if form.is_valid():
#             phone = form.cleaned_data['phone']
#             try:
#                 user = player.objects.get(phone=phone)
#                 user.front_image = form.cleaned_data['front_image']
#                 user.back_image = form.cleaned_data['back_image']
#                 user.kyc_status = 'In Progress'
#                 user.save()
#                 messages.success(request, 'KYC documents uploaded successfully.')
#                 return redirect('ludoapp:landing')
#             except player.DoesNotExist:
#                 messages.error(request, 'Player with this phone number does not exist.')
#         else:
#             print("Form is not valid")
#             print(form.errors)
#     else:
#         form = kycForm()
    
#     return render(request, 'kyc.html', {'form': form})


def kyc(request):
    phone = request.session.get('phone')
    print(phone)
    if request.method == 'POST':
        form = kycForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                user = player.objects.get(phone=phone)
                user.front_image = form.cleaned_data['front_image']
                user.back_image = form.cleaned_data['back_image']
                user.kyc_status = 'In Progress'
                user.save()
                messages.success(request, 'KYC documents uploaded successfully.')
                return redirect('ludoapp:landing')  # Redirect to landing page or wherever you need
            except player.DoesNotExist:
                messages.error(request, 'Player with this phone number does not exist.')
        else:
            print("Form is not valid")
            print(form.errors)
    else:
        form = kycForm()
    
    return render(request, 'kyc.html', {'form': form, 'phone': phone})

        # print("supplier post method is working")
        # form = kycForm(request.POST,request.FILES)
        # if form.is_valid():
        #     # phone = form.cleaned_data['phone']
        #     # front_image = form.cleaned_data['front_image']
        #     # back_image = form.cleaned_data['back_image']

        #     # Check if the player exists with the given phone number
        #     try:
        #         user = player.objects.get(phone=phone)
        #         user.phone = form.cleaned_data['phone']
        #         user.front_image = form.cleaned_data['front_image']
        #         user.back_image = form.cleaned_data['back_image']
        #         # user.front_image = front_image
        #         # user.back_image = back_image
        #         # Optionally, you can update the KYC status here if needed
        #         # user.kyc_status = 'pending'
        #         user.save()
        #         print("data adhar saved")
        #         print(front_image)
        #         # messages.success(request, 'KYC documents uploaded successfully.')
        #         return redirect('ludoapp:landing', phone=phone)
        #     except player.DoesNotExist:
        #         messages.error(request, 'Player with this phone number does not exist.')
            # print("supplier Form is valid form")
            # user = player.objects.filter(phone=player_phone).first()
            # user.phone = form.cleaned_data['phone']
            # user.front_image = form.cleaned_data['front_image']
            # user.back_image = form.cleaned_data['back_image']
            # # user.kyc_status = 'pending'
            # user.save()
    #     else:
    #         print("Form is not valid")
    #         print(form.errors)
    #         # error_message = "upload correctly"
    #         # messages.error(request, error_message)
    #         return render(request, 'kyc.html') #, {'error_message': error_message})
    # else:
    #     print("post method not right")
    #     form = kycForm()
    #     return render(request,'kyc.html')


# from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
# from .forms import UserProfileForm

# @login_required
def edit_profile(request):
    # if request.method == 'POST':
    #     form = UserProfileForm(request.POST, instance=request.user)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('profile')
    # else:
    #     form = UserProfileForm(instance=request.user)
    return render(request, 'edit_profile.html') #, {'form': form})


def wallet(request):
    phone = request.session.get('phone')
    player_instance = player.objects.get(phone=phone)
    return render(request,'wallet.html',{'player_instance':player_instance})

def profile_edit(request):
    return render(request,'profile_edit.html')



def history(request):
    return render(request,'history.html')

def indexfirst(request):
    return render(request,'indexfirst.html')

# def login_page(request):
#     if request.method == 'POST':
#         print("post method is working")
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             print("Form is valid form")
#             phone = form.cleaned_data['phone']
#             password = form.cleaned_data['password']
#             user = player.objects.filter(phone=phone).first()
#             if user and check_password(password, user.password): # and user.Approvance_Status==True:
#                 print("Login Successful")
#                 # Login successful, redirect to home page
#                 return redirect('ludoapp:landing')
#             else:
#                 print("Login failed") # , show error message
#                 # return HttpResponse("Invalid username or password")
#                 error_message = "Invalid phone number or password"
#                 messages.error(request, error_message)
#                 return render(request, 'login_page.html', {'form': form, 'error_message': error_message})
#         else:
#             print("form is not valid")
#             print(form.errors)
#             return redirect('ludoapp:login_page')
#     else:
#         print("post method is not working")
#         form = LoginForm()
#         return render(request, 'login_page.html' ,{'form': form})
#     # return render(request,'login_page.html')


def login_page(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            phone = form.cleaned_data['phone']
            password = form.cleaned_data['password']
            user = player.objects.filter(phone=phone).first()
            if user and check_password(password, user.password):
                request.session['phone'] = phone
                # print(phone)  # Save phone number in session
                return redirect('ludoapp:landing')
            else:
                error_message = "Invalid phone number or password"
                messages.error(request, error_message)
                return render(request, 'login_page.html', {'form': form, 'error_message': error_message})
        else:
            print("Form is not valid")
            print(form.errors)
    else:
        form = LoginForm()
    return render(request, 'login_page.html', {'form': form})


def registration_page(request):
    if request.method=='POST':
        form = playerForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']
            if password == confirm_password:
                user.password = make_password(password)
                user.save()
                print("dAta asaved")
                # send_approval_email(player.user.player_email)
                return redirect('ludoapp:login_page')
            else:
                return redirect('ludoapp:registration_page')
        else:
            print("Form is not valid")
            print(form.errors)
            return redirect('ludoapp:registration_page')
    else:
        form = playerForm()
        print("Rendering form")
        return render(request , 'registration_page.html')

    # return render(request,'registration-page.html')

def adminpanel(request):
    return render(request,'adminpanel.html')
