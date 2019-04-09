from django.shortcuts import render,redirect
from .forms import RegistrationForm,LoginForm
from.models import RegistrationData
from django.http.response import HttpResponse

# Create your views here.
def registration_view(request):
    if request.method=="POST":
        rform=RegistrationForm(request.POST)
        if rform.is_valid():
            f_name=request.POST.get('first_name','')
            l_name=request.POST.get('last_name','')
            mob_no=request.POST.get('mobile','')
            email=request.POST.get('email','')
            u_name=request.POST.get('usernamerf','')
            pass_1=request.POST.get('password1','')
            pass_2=request.POST.get('password2','')

            data=RegistrationData(
                first_name=f_name,
                last_name=l_name,
                mobile_no=mob_no,
                email=email,
                usernamed=u_name,
                passwordd=pass_1,
                password2=pass_2,
            )
            data.save()
            lform=LoginForm()
            return render(request,'login.html',{'lhform':lform})
        else:
            return HttpResponse("invalid form")
    else:
        rform=RegistrationForm()
        return render(request,'registration.html',{'rform':rform})
def login_view(request):
    if request.method=="POST":
        lform=LoginForm(request.POST)
        if lform.is_valid():
            uname=request.POST.get('usernamel','')
            pswd=request.POST.get('password11','')
            uname1=RegistrationData.objects.filter(usernamed=uname)
            pass1=RegistrationData.objects.filter(passwordd=pswd)
            if uname1 and pass1:
                return redirect(home_view)
            else:
                return HttpResponse("invalid")
    else:
        lform=LoginForm()
        return render(request,'login.html',{'lhform':lform})



def home_view(request):
    return HttpResponse('welcome to site')
