from django.shortcuts import render
from twilio.rest import Client
# Create your views here.

account_sid = "ACec66462ecdad794f85ae2cd409363a83"
auth_token = "4208c5a3f6899b42ecd60bfc0a4d5778"
client = Client(account_sid, auth_token)


# print(message.sid)

def Home(request):
    return render(request, "index.html", context={})

def Redeem(request):
    message = client.messages \
                .create(
                     body="Congratulations, here is your reward 🚀. You can use the code:AHJ34J at McDonald's to get discount",
                     from_='+16072845966',
                     to='+917977675557'
                 )
    print(message.sid)
    return render(request, "redeem.html", context={})