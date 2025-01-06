from django.shortcuts import render , redirect
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout
from django.contrib import messages
from .models import *
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
# Create your views here.

def user_register(request):
    if request.method == 'POST' :
        form = UserRegisterForm(request.POST)
        if form.is_valid() :
            data = form.cleaned_data
            user = User.objects.create_user(
                username = data['user_name'] ,
                email = data['email'] ,
                first_name = data['first_name'],
                last_name = data['last_name'] ,
                password = data['password_2']
            )
            user.save()
            messages.success(request , 'ثبت نام شما با موفقیت انجام شد'  ,'success')
            return redirect('blog:post_show')
    else :
        form = UserRegisterForm
    return render(request , 'register.html',{'form':form})




def user_login(request) :
    if request.method == 'POST' :
        form = UserLoginForm(request.POST)
        if form.is_valid() :
            data = form.cleaned_data
            user = authenticate(request ,
                                username = data['user'] , password = data['password'])
            if user is not None :
                login(request , user)
                messages.success(request , 'خوش آمدید' , 'primary')
                return redirect('accounts:profile')
            else:
                messages.error(request , 'نام کاربری یا رمز عبور اشتباه است' , 'danger')

    else :
        form = UserLoginForm
    return render(request,'login.html',{'form':form})

def user_logout(request):
    logout(request)
    messages.success(request,'به امید دیدار' , 'info')
    return redirect('blog:post_show')

@login_required(login_url='accounts:login')
def profile(request):
    profile = Profile.objects.get(user_id=request.user.id)
    return render(request , 'profile.html' , {'profile':profile})

@login_required(login_url='accounts:login')
def update_profile(request):
    if request.method == 'POST':
        user_form = Updateuserform(request.POST,instance=request.user)
        profile_form = UpdateProfileForm(request.POST,request.FILES,instance=request.user.profile)
        if user_form and profile_form.is_valid() :
            user_form.save()
            profile_form.save()
            return redirect('accounts:profile')
    else :
        user_form = Updateuserform(instance=request.user)
        profile_form = UpdateProfileForm(instance= request.user.profile)
    return render(request , 'update.html',
                  {'user_form':user_form ,'profile_form':profile_form})
# def update_profile(request) :
#     if request.method == 'POST' :
#         update_user = Updateuserform(request.POST,instance=request.user)
#         update_profile = UpdateProfileForm(request.POST , request.FILES,instance=request.user.profile)
#         if update_user and update_profile.is_valid():
#             update_user.save()
#             update_profile.save()
#             return redirect('accounts:profile')
#     else:
#         update_user = Updateuserform(instance=request.user)
#         update_profile = UpdateProfileForm(instance=request.user.profile)
#     return render(request , 'update.html' , {'update_user' : update_user , 'update_profile' : update_profile})

@login_required(login_url='accounts:login')
def change_pass(request) :
    if request.method == 'POST' :
        form = PasswordChangeForm(request.POST , request.user)
        if form.is_valid:
            form.save()
            update_session_auth_hash((request , form.user))
            return redirect('accounts:profile')

    else:
        form = PasswordChangeForm(request.user)
        return render(request , 'change.html' , {'form' : form})