from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def leshka(request):
    return render(request, 'lexa/leshka.html')
def klyatov(request):
    ip = request.META.get('HTTP_X_FORWARDED_FOR') or request.META.get('REMOTE_ADDR')
    user_info = request.META.get('Http_USER_AGENT')
    return render(request, 'lexa/klyatov.html',locals())
