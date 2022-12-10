from django.shortcuts import render, redirect
from .models import Insurances, InsuredMembers
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .admin import *
from itertools import chain
from .forms import InsuranceForm, InsuredMembersForm, AddressForm


def index(request):
    if request.method == 'POST':

        u=authenticate(username=request.POST['username'],password=request.POST['password'])
        if u is not None:
            login(request,u)
            return redirect('home')
        else:
            form1 = AuthenticationForm()
            return render(request, 'form.html', {'form1': form1,'msg':'invalid credentials'})
    else:
        form1 = AuthenticationForm()
        return render(request, 'form.html', {'form1': form1})


def user_login(request):
    if request.method=='POST':
        user = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=user, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            message = 'invalid credentials'
            form = AuthenticationForm()
            return render(request, 'form.html', {'msg':message,'form':form})
    else:
        form = AuthenticationForm()
        return render(request,'form.html', {'form':form})





def insurance(request):
    if not request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        form = InsuranceForm(request.POST)
        form2 = InsuredMembersForm(request.POST)
        form3 = AddressForm(request.POST)
        if not form2.is_valid():
            form = InsuranceForm(request.POST,initial={'cust_key':request.POST['cust']})
            form3 = AddressForm(request.POST,initial={'cust':request.POST['cust']})
            return render(request, 'insurance.html', {'form1': form, 'form2': form2, 'form3': form3})
        form2.save()
        if form.is_valid() and form3.is_valid():
            form.save()
            form3.save()
            msg='Insurance generated successfully'
            id = InsuredMembers.objects.all().last()
            if id:
                id = str(int(id.cust_id) + 1)
            else:
                id = str(1)
            form1 = InsuranceForm(initial={'cust_key': id})
            form2 = InsuredMembersForm(initial={'agnt': request.user, 'cust_id': id})
            form3 = AddressForm(initial={'cust': id})
            return render(request, 'insurance.html', {'msg': msg, 'form1': form1, 'form2': form2, 'form3': form3})
        else:
            InsuredMembers.objects.all().last().delete()
            return render(request, 'insurance.html', {'form1': form, 'form2': form2,'form3':form3})
    else:
        id = InsuredMembers.objects.all().last()
        if id:
            id = str(int(id.cust_id)+1)
        else:
            id = str(1)
        form1 = InsuranceForm(initial={'cust_key':id})
        form2 = InsuredMembersForm(initial={'agnt':request.user,'cust_id':id})
        form3 = AddressForm(initial={'cust':id})
        return render(request, 'insurance.html', {'form1': form1, 'form2': form2, 'form3': form3})


def register(request):
    if request.method =='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'info.html',{'msg':'Account was created plz Login'})
        else:
            return render(request, 'form.html', {'form1': form, 'af':'0'})

    else:
        form = UserCreationForm()
        return render(request, 'form.html', {'form1': form,'af':'0'})


def home(request):
    if not request.user.is_authenticated:
        return redirect('index')
    return render(request, 'home.html',)




def insmem(request):
    if not request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        id=request.POST['id']
        try:
            mem=InsuredMembers.objects.get(cust_id=id)

            mem.delete()
            return redirect('insmem')
        except:
            return redirect('insmem')

    else:
        memdata = InsuredMembers.objects.filter(agnt__username=request.user)
        return render(request,'insdata.html',{'memsdata':memdata})


def insdata(request):
    if not request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        id=request.POST['custid']
        try:
            insm=InsuredMembers.objects.get(cust_id=id)
            insm.delete()
            return redirect('insdata')
        except:
            return redirect('insdata')

    else:
        insrdata = InsuredMembers.objects.filter(agnt__username=request.user)
        return render(request,'insdata.html',{'insdata':insrdata})