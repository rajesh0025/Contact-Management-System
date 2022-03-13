from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponseRedirect
from . import forms,models
from django.http import HttpResponseRedirect
from django.contrib.auth.models import Group
from django.contrib import auth
from django.contrib.auth.decorators import login_required,user_passes_test


def adminsignup_view(request):
    form=forms.AdminSigupForm()
    if request.method=='POST':
        form=forms.AdminSigupForm(request.POST)
        if form.is_valid():
            user=form.save()
            user.set_password(user.password)
            user.save()

            my_admin_group = Group.objects.get_or_create(name='ADMIN')
            my_admin_group[0].user_set.add(user)

            return HttpResponseRedirect('adminlogin')
    return render(request,'app/adminsignup.html',{'form':form})


def is_admin(user):
    return user.groups.filter(name='ADMIN').exists()

def afterlogin_view(request):
    if is_admin(request.user):
        return render(request,'app/adminafterlogin.html')
    else:
        return render(request,'app/logout.html')

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def addcontact_view(request):
    #now it is empty book form for sending to html
    form=forms.ContactForm()
    if request.method=='POST':
        #now this form have data from html
        form=forms.ContactForm(request.POST)
        if form.is_valid():
            user=form.save()
            return render(request,'app/contactadded.html')
    return render(request,'app/addcontact.html',{'form':form})

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def viewcontact_view(request):
    contacts=models.Contact.objects.all()
    return render(request,'app/viewcontact.html',{'contacts':contacts})

