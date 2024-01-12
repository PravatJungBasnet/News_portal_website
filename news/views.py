from django.shortcuts import render,HttpResponseRedirect
from .models import Category,news
from .forms import UserCreationForm,User,newsform
from django.contrib.auth.forms import AuthenticationForm,SetPasswordForm
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages

# Create your views here.
#showind data in dashboard
def dashboard(request):
    first_news=news.objects.all().order_by('-created_at')[0]
    three_news=news.objects.all()[1:3]
    category_news=Category.objects.all()[0:3]

    return render(request,'news/dashboard.html',{'first_news':first_news,'three_news':three_news,'category_news':category_news})



#fetching sll news
def all_news(request):
    all=news.objects.all().order_by('-created_at')
    search=request.GET.get('search_area','')
    if search:
        all=Category.objects.filter(title__icontains=search,)
        
    return render(request,'news/allnews.html',{'all':all,})





#all category
def all_category(request):
    all_cate=Category.objects.all()
    return render(request,'news/allcategory.html',{'all_cate':all_cate})

# detail of selected news and news related to them
def detail_news(request,id):
    detail=news.objects.get(pk=id)
    category=Category.objects.get(id=detail.category.id)
    rel_news=news.objects.filter(category=category).exclude(id=id).order_by('-created_at')

    return render(request,'news/detail.html',{'detail':detail,'category':category,'rel_news':rel_news,})



#signup
def user_signup(request):
    if request.method=='POST':
        fm=UserCreationForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.add_message(request,messages.SUCCESS,'Invalid username or password')
            
            return HttpResponseRedirect('/log/')
            


    else:
        fm=UserCreationForm()
    return render(request,'news/signup.html',{'fm':fm})
    

#login
def user_login(request):
    if request.method=='POST':
        fm=AuthenticationForm(request=request,data=request.POST)
        if fm.is_valid():
            uname=fm.cleaned_data['username']
            upass=fm.cleaned_data['password']
            user=authenticate(username=uname,password=upass)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect('/')
        else:
            messages.add_message(request,messages.SUCCESS,'Incorrect  username or password')
    else:
        fm=AuthenticationForm()
    return render(request,'news/login.html',{'fm':fm})

# logout
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


#Add news
def add_news(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            fm=newsform(request.POST,request.FILES)
            if fm.is_valid():
                fm.instance.user=request.user
                fm.save()
                return HttpResponseRedirect('/')
        else:
            fm=newsform()
        return render(request,'news/addnews.html',{'fm':fm})
#edit/update
def update(request,id):
    if request.user.is_authenticated:

        if request.method=='POST':
            pi=news.objects.get(pk=id)
            fm=newsform(request.POST,instance=pi)
            if fm.is_valid():
                fm.save()
                return HttpResponseRedirect('/')
        else:
            pi=news.objects.get(pk=id)
            fm=newsform(instance=pi)
        return render(request,'news/update.html',{'fm':fm})
#delete news 
    
def delete(request,id):
    if request.user.is_authenticated:
        pi=request.objects.get(pk=id)
        if request.method=='POST':
            pi.delete()
            return HttpResponseRedirect('/')
#FForgot password
def change_pass(request):
    if request.method=='POST':
        fm=SetPasswordForm(user=request.user,data=request.POST)
        if fm.is_valid:
            fm.save()
            return HttpResponseRedirect('/log/')
    else:
        fm=SetPasswordForm(user=request.user)
    return render(request,'news/newpass.html',{'fm':fm})
               


        