from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .forms import loginform,registerform
# Create your views here.

def login_view(request):
    if request.user.is_authenticated:
        return redirect("/")
    form = loginform(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username,password=password)
        login(request,user)
        return redirect('base')
    return render(request,'logintemp.html',{'form':form,'title':'Giris'})


# def register_view(request):
#     form = loginform(request.POST or None)
#     if form.is_valid():
#         user = form.save(commit = False)
#         #username = form.cleaned_data.get('username')
#         password = form.cleaned_data.get('password1')
#         user.set_password(password)
#         user.save()
#         new_user = authenticate(username = user.username,password = password)
#         login(request,new_user)
#         return redirect('base')
#     return render(request,'logintemp.html',{'form':form,'title':'Qeydiyyatdan Kec'})

def register_view(request):
    if request.user.is_authenticated:
        return redirect("/")
    form = registerform(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password1')
        user.set_password(password)
        # user.is_staff = user.is_superuser = True
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        return redirect('base')
    return render(request, "logintemp.html", {"form": form, 'title': 'Qeydiyyatdan Kec'})


def logout_view(request):
    logout(request)
    return redirect('base')






