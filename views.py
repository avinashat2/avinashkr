from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from .models import Post ,Comment



# Create your views here.

def Index(request):
    posts=Post.objects.all()
    return render(request,'index.html',{'posts':posts})


def Signuphandle(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
        if len(username) > 20 :
            messages.warning(request,'username lenth is too high !')
            return redirect('signup')
        if User.objects.filter(username=username).exists():
            messages.warning(request,'username is already taken')
            return redirect('signup')
        if password1==password2 :
            user=User.objects.create_user(username=username,password=password1)
            messages.success(request,'Signup Success !')
            return redirect('index')
        messages.error(request,'Password does not matched !')
        return redirect('signup')
    return render(request,'signup.html')


def Loginhandle(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password = request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            # messages.success(request,'logged in success')
            return redirect('index')
        messages.error(request,'INVALID USER !  ')
        return redirect('login')
    return render(request,'login.html')

@login_required
def Logouthandle(request):
    logout(request)
    messages.success(request,'logged out success !')
    return redirect('index')



@login_required
def Addpost(request):
    if request.method=='POST':
        
        title=request.POST.get('title')
        content=request.POST.get('content')

        if len(title)>200:
            messages.error(request,'title length is more than 200')
            return redirect('addpost')
        post=Post(title=title,content=content,user=request.user)
        post.save()
        messages.success(request,'Post Created success')
        return redirect('addpost')
    return render(request,'addpost.html')

    
@login_required
def Readpost(request,id):
    print(id)
    cmn = Comment.objects.all()
    post=Post.objects.get(id=id)
    return render(request,'post.html',{'post':post,"comments":cmn})

@login_required
def CommentView(request,id):
    post=Post.objects.get(id=id)
    if request.method=="POST":
        post=Post.objects.get(id=id)
        comments=request.POST.get('comments')
        cmnt=Comment(user=request.user,post=post,comments=comments)
        cmnt.save() 
        return redirect(reverse('readpost', kwargs={"id": id}))
    return redirect('readpost',{"id":id})
 