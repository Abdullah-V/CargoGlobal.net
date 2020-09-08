from django.shortcuts import Http404, render,HttpResponse,get_object_or_404,HttpResponseRedirect,redirect
from .models import elan
from .forms import elanform
# from .forms import postform
from django.contrib import messages
from django.db.models import Q
from datetime import datetime, time, date, timedelta
import datetime
from django.utils import timezone
from django.core.paginator import Paginator
# Create your views here.


def elanlar(request):
    elanlar = elan.objects.all()
    for birtaskelan in elanlar:
        if birtaskelan.silinme_vaxti < timezone.now():
            birtaskelan.delete()

    sorgu = request.GET.get("query")
    if sorgu:
        elanlar = elanlar.filter(
            Q(cixis_yeri__icontains = sorgu)|
            Q(catma_yeri__icontains = sorgu)|
            Q(cixis_vaxti__icontains = sorgu)|
            Q(catma_vaxti__icontains = sorgu)
        )
        
    context = {
        'elanlar':elanlar,
    }
    return render(request,'elanlar.html',context)


def elaveet(request):
    if not request.user.is_authenticated:
        return redirect('/hesablar/qeydiyyat')

    form = elanform(request.POST or None)

    if form.is_valid():
        post = form.save(commit=False)
        post.user = request.user
        post.silinme_vaxti = timezone.now() + timedelta(days=10)
        form.save()
        messages.success(request,"Elan Əlave Edildi!")
        return redirect('base')

    else:
        form = elanform()

    context = {
        'form':form,
        'title':'Elan Əlave Et',
        'btntext':'Əlave Et',
    }
    return render(request,'form.html',context)    
        
    
def detallar(request,id):
    detalelan = get_object_or_404(elan,id=id)
    elanlar = elan.objects.all()
    elanlar = elanlar.filter(
        Q(cixis_yeri__icontains = detalelan.cixis_yeri)|
        Q(catma_yeri__icontains = detalelan.catma_yeri)|
        Q(cixis_vaxti__icontains = detalelan.cixis_vaxti)|
        Q(catma_vaxti__icontains = detalelan.catma_vaxti)
    )
    if detalelan.sirket:
        elanlar = elanlar.filter(
            Q(sirket__icontains = detalelan.sirket)
        )
    elanlar = elanlar.exclude(
        # Q(cixis_yeri = detalelan.cixis_yeri)&
        # Q(catma_yeri = detalelan.catma_yeri)&
        # Q(cixis_vaxti = detalelan.cixis_vaxti)&
        # Q(catma_vaxti = detalelan.catma_vaxti)&
        # Q(elaqe_nomresi = detalelan.elaqe_nomresi)&
	    Q(id = detalelan.id)
    )
    sayi = len(elanlar)
    return render(request,'detallar.html',{'detalelan':detalelan,'elanlar':elanlar,'sayi':sayi})





def menimelanlarim(request):
    if not request.user.is_authenticated:
        return redirect('/hesablar/qeydiyyat')
    requser = request.user
    requserelan = elan.objects.filter(user = requser)
    return render(request,'menimelan.html',{'requserelan':requserelan})



def deyisdir(request,id):
    if not request.user.is_authenticated:
        return redirect('/hesablar/qeydiyyat')

    elanobje = get_object_or_404(elan,id=id)
    if elanobje.user == request.user:
        form = elanform(request.POST or None,instance=elanobje)
    else:
        return redirect('/')
    if form.is_valid():
        save = form.save()
        messages.success(request,'Elan Deyisdirildi!')
        return HttpResponseRedirect('/menimelanlarim')
    context = {
        'form':form,
        'title':'Elanı Dəyişdir',
        'btntext':'Dəyişdir',
    }
    return render(request,'form.html',context)
    


def sil(request,id):
    if not request.user.is_authenticated:
        return redirect('/hesablar/qeydiyyat')
    elanobje = get_object_or_404(elan,id=id)
    if elanobje.user == request.user:
        elanobje.delete()
        messages.success(request,'Elan Silindi!')
        return redirect('/menimelanlarim')
    else:
        return redirect('/')
    


def favoritview(request,id):
    # favelan = get_object_or_404(elan,id = id)
    # if request.user.favorit(favelan).exists():
    #     request.user.favorit.remove(favelan)
    # else:
    #     request.user.favorit.add(favelan)
    # return redirect("/")
    # hindininki
    if request.user.is_authenticated:
        favelan = get_object_or_404(elan,id = id)
        isfav = True
        if favelan.favorit.filter(id = request.user.id).exists():
            favelan.favorit.remove(request.user)
            messages.success(request,'Elan Uluzlulardan Silindi!')
            isfav = False
            # request.META['HTTP_REFERER']
            return HttpResponseRedirect(request.META['HTTP_REFERER'])
        else:
            favelan.favorit.add(request.user)
            messages.success(request,'Elan Uluzlulara Elave Olundu!')
            isfav = True
            # request.META['HTTP_REFERER']
            return HttpResponseRedirect(request.META['HTTP_REFERER'])
    return redirect('/hesablar/qeydiyyat')



def favelanlar(request):
    if request.user.is_authenticated:
        favelanlar = request.user.favorit.all()
        return render(request,'favelanlar.html',{'favelanlar':favelanlar})
    else:
        return redirect('/hesablar/qeydiyyat')
  


def komek(request):
    return render(request,'komek.html',{})


def haqqinda(request):
    return render(request,'haqqinda.html',{})



# error handlers


def page_404(request,exception):
    return render(request, '404.html')


# *101#579589493059358# yes
