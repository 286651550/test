from django.shortcuts import render
from django.shortcuts import HttpResponse
from blog import models
from itertools import chain
import random

# Create your views here.

user_list = [
    {"user":"jack","pwd":"abc"},
    {"user":"tom","pwd":"ABC"},
]

aa_list = [
]



def index(request):
    #return HttpResponse("hello world!")
    choucha_list = [
]
    global user_list
    global aa_list
    # if request.method=="POST":
        # username = request.POST.get("username", None)
        # password = request.POST.get("password",None)
        # models.UserInfo.objects.create(user=username, pwd=password)
        #aa_list = models.Article.objects.all()
        # user_list = models.UserInfo.objects.all()
        # models.UserInfo.objects.create(user=username, pwd=password)
    if request.method=="POST":
         mumuzu = int(request.POST.get("mumuzu", None))
         jiajiazu = int(request.POST.get("jiajiazu",None))
         wanwanzu = int(request.POST.get("wanwanzu",None))
         #choucharenshu = mumuzu + jiajiazu
         #choucha_list = random.sample(models.Article.objects.all().values('title'), sum)
         mumuzu_list = models.People.objects.filter(shifouchoucha='是',fenzu='木木').order_by('?')[:mumuzu]
         jiajiazu_list = models.People.objects.filter(shifouchoucha='是',fenzu='佳佳').order_by('?')[:jiajiazu]
         wanwanzu_list = models.People.objects.filter(shifouchoucha='是',fenzu='绾绾').order_by('?')[:wanwanzu]
         choucha_list = chain(mumuzu_list, jiajiazu_list, wanwanzu_list)

    aa_list = models.People.objects.all()
    #return render(request, "index.html", {"data":user_list})
    return render(request, "index.html",{"data":aa_list,"data1":choucha_list})