from django.conf import settings
# from django.contrib.auth.views import LoginView, LogoutView
from django.conf.urls.static import static
from django.urls import path
from . import views 

app_name = 'ludoapp'

urlpatterns = [
    path('', views.indexfirst, name='indexfirst'),
    path('indexlogin/', views.indexlogin, name='indexlogin'),
    path('landing/', views.landing, name='landing'),
    path('demo/', views.demo, name='demo'),
    path('demo/', views.demo, name='demo'),
    path('kyc/', views.kyc, name='kyc'),
    path('playerdetail/', views.playerdetail, name='playerdetail'),
    path('send_otp/', views.send_otp, name='send_otp'),
    path('verify_otp/', views.verify_otp, name='verify_otp'),
    path('profile/', views.edit_profile, name='profile'),
    path('profile_edit/', views.profile_edit, name='profile_edit'),
    path('wallet/', views.wallet, name='wallet'),
    path('history/', views.history, name='history'),
    path('index/', views.index, name='index'),
    path('login_page/', views.login_page, name='login_page'),
    path('registration_page/', views.registration_page, name='registration_page'),
    path('adminpanel/', views.adminpanel, name='adminpanel'),
    path('battle/', views.battle, name='battle'),
    path('battle', views.play_battle, name='play_battle'),
    path('accept/<int:battle_id>/', views.accept_battle, name='accept_battle'),
    path('policy/', views.policy, name='policy'),
    path('refer/', views.refer, name='refer'),
    path('support1/', views.support1, name='support1'),
    path('addmoney/', views.addmoney, name='addmoney'),
    path('approve/<str:phone>/', views.approve_player, name='approve_player'),
    path('delete/<str:phone>/', views.delete_player, name='delete_player'),
    path('share/whatsapp/', views.share_whatsapp, name='share_whatsapp'),
    path('share/telegram/', views.share_telegram, name='share_telegram'),
    path('copy_refer_code/', views.copy_refer_code, name='copy_refer_code'),
    path('withdrawal/', views.withdrawal, name='withdrawal'),
    path('withdrawalaccount/', views.withdrawalaccount, name='withdrawalaccount'),
    # path('playbattle', views.playbattle, name='playbattle'),
    path('viewbattle/', views.viewbattle, name='viewbattle'),
    path('setbattle/', views.setbattle, name='setbattle'),
    path('battle_landing/', views.battle_landing, name='battle_landing'),
    # path('battle/', views.play_battle_view, name='play_battle_view'),
    path('accept_battle_view/', views.accept_battle_view, name='ludoapp:accept_battle_view'),
    path('delete_battle_view/', views.delete_battle_view, name='ludoapp:delete_battle_view'),
    # path('battle/', views.create_battle, name='create_battle'),
    # path('battle/play/<int:battle_id>/', views.play_battle, name='play_battle'),
    # path('battle/accept_or_abort/<int:battle_id>/', views.accept_or_abort_request, name='accept_or_abort_request'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Add Django auth views for login and logout
# urlpatterns += [
#     path('accounts/login/', LoginView.as_view(), name='login_page'),  # Default Django login view
#     path('accounts/logout/', LogoutView.as_view(), name='logout'),  # Default Django logout view
# ]