from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Employee
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

@login_required
def home(request):
    return render(request,"index.html")

def sign_up(request):
    try:
        form = UserCreationForm(request.POST)
        if request.method =='POST':
            if form.is_valid():
                form.save()
                return redirect('login')
            return render(request,"sign_up.html",{'form':userform,'msg':"invalid login"})
        else:
            return render(request,"sign_up.html",{'form':userform,'msg':"invalid submission"})
    except Exception as e:
        print(e)
        userform=UserCreationForm()
        return render(request,"sign_up.html",{'form':userform})
    

def loginview(request):
    uname=request.POST['username']
    pwd=request.POST['password']
    user=authenticate(request,username=uname,password=pwd)
    if user is not None:
        login(request,user)
        return redirect('home')
    else:
        return render(request,"login.html",{"msg":"invalid login"})
    

def logout_view(request):
    logout(request)
    return redirect('login')


def Resethome(request):
    return render(request,'ResetPassword.html')

def resetPassword(request):
    uname=request.POST['uname']
    newpwd=request.POST['password']
    try:
        user=User.objects.get(username=uname)
        if user is not None:
            user.set_password(newpwd)
            user.save()
            return render(request,"ResetPassword.html",{"errmsg":"password reset successfully"})
    except Exception as e:
        print(e)
        return render(request,"ResetPassword.html",{"errmsg":"Password reset failed"})


def addEmployee(request):
    try:
        Name=request.POST['name']
        Address=request.POST['address']
        Age=int(request.POST['age'])
        empobj=Employee.objects.create(name=Name,address=Address,age=Age)#instead of insert query
        empobj.save()#to save in the table built in func
        return render(request,"index.html",{"msg":"Employee added"})
    except Exception as e:
        print(e)
        return render(request,"index.html",{"msg":"Employee can't be added"})#try except is used to show any error without displaying error in a page

#read
def display(request):
    empdtls=Employee.objects.all()#instead of select query
    return render(request,"index.html",{"emp":empdtls})

#delete using name
def delemployee(request):
    empname=request.POST['name']
    empdtls=Employee.objects.filter(name=empname)
    if empdtls.exists():
        empdtls.delete()
        return render(request,"index.html",{"msg":"Deleted"})
    else:
        return render(request,"index.html",{"msg":"No records found"})
    

def updatename(request):
    try:
        oldname=request.POST["oldname"]
        newname=request.POST["newname"]
        emp=Employee.objects.filter(name=oldname)
        if emp.exists():
            emp.update(name=newname)
            return render(request,"index.html",{"msg":"updated"})
        else:
            return render(request,"index.html",{"msg":"no records found"})
    except Exception as e:
        print(e)
        return render(request,"index.html",{"msg":"Not updated"})
    

