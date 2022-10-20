import datetime

from django.db.models import Q
from django.shortcuts import render
from myfiles.models import *
# Create your views here.

def home(malumot):
    if malumot.method == "POST":
        matn = malumot.POST.get('search')
        soz= str(matn).strip()
        malumot1 = Q(nomi__startswith = soz)|Q(manzil__startswith = soz)|Q(xona1__startswith = soz)|Q(xona2__startswith = soz)|Q(kv__startswith = soz)|Q(rasm__startswith=soz)|Q(narx_old__startswith = soz)|Q(narx_new__startswith = soz)
        malumot2 = Q(ismi__startswith = soz)|Q(ishi__startswith = soz)|Q(men_haqimda__startswith=soz)|Q(rasm__startswith = soz)
        malumot3 = Q(name__startswith = soz)|Q(mulki__startswith = soz)|Q(rasm__startswith = soz)
        malumot4 = Q(rasm__startswith=soz) | Q(malumot__startswith=soz) | Q(sana__startswith=soz)
        ish = Work.objects.filter(malumot1).order_by('-id')[:3]
        klent = Clients.objects.filter(malumot2)
        agentlar = Agents.objects.filter(malumot3).order_by('-id')[:4]
        o_ishlar = Oxirgi_ishlar.objects.filter(malumot4)
        return render(malumot, 'index.html', {'ishlar': ish, 'klents': klent, 'agentl': agentlar, 'ox_ishlar': o_ishlar})
    else:
        ish=Work.objects.all().order_by('-id')[:3]
        klent=Clients.objects.all()
        agentlar=Agents.objects.all().order_by('-id')[:4]
        o_ishlar=Oxirgi_ishlar.objects.all()
        return render(malumot,'index.html', {'ishlar':ish,'klents':klent,'agentl':agentlar,'ox_ishlar':o_ishlar})

def agent(malumot1):
    if malumot1.method == "POST":
        matn1 = malumot1.POST.get('a_search')
        soz1 = str(matn1).strip()
        malumot_a = Q(name__startswith = soz1)|Q(mulki__startswith = soz1)|Q(rasm__startswith = soz1)
        agentlar = Agents.objects.filter(malumot_a)
        return render(malumot1,'agent.html',{'agent':agentlar})
    else:
        agentlar = Agents.objects.all()
        return render(malumot1, 'agent.html',{'agent':agentlar})

def contact(malumot2):

    if malumot2.method=='POST':
        sname = malumot2.POST.get("ism")
        gmail = malumot2.POST.get("mail")
        subjact = malumot2.POST.get("sub")
        message = malumot2.POST.get("message")
        vaqtga = datetime.datetime.now()
        Murojaat(ism=sname, mail=gmail, sub=subjact, mess=message, vaqt=vaqtga).save()
    return render(malumot2,'contact.html' )

def properties(malumot3):
    if malumot3.method == 'POST':
        matn2 = malumot3.POST.get('p_search')
        soz2 = str(matn2).strip()
        malumot_p = Q(nomi__startswith=soz2) | Q(manzil__startswith=soz2) | Q(xona1__startswith=soz2) | Q(xona2__startswith=soz2) | Q(kv__startswith=soz2) |Q(rasm__startswith=soz2) | Q(narx_old__startswith=soz2) | Q(narx_new__startswith=soz2)
        ish = Work.objects.filter(malumot_p).order_by('-id')
        return render(malumot3, 'properties.html', {'ish': ish})
    else:
        ish = Work.objects.all().order_by('-id')[3:]
        return render(malumot3,'properties.html',{'ish':ish})

def properties_single(malumot4):
    return render(malumot4,'properties-single.html')