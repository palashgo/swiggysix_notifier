from django.http import HttpResponse
from django.shortcuts import render
from webpush import send_group_notification


def index(request):
    webpush = {"group": "sixers"}
    return render(request, 'template.html', {"webpush": webpush})

def sendsixalert(request):
    payload = {"head": "SIX Notifier", "body": "Its a 6. Order within next 6 mins"}
    send_group_notification(group_name="sixers", payload=payload, ttl=1000)
    return HttpResponse("")
