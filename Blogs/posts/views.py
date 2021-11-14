from django.shortcuts import render,get_object_or_404,redirect
from posts.models import contact_us,Poster,contact_us,Author
from posts.forms import *
from django.http import HttpResponse,HttpResponseRedirect
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.contrib.auth import authenticate,login,get_user_model,logout

# Create your views here.

# def index(request):
#     return render(request,'index.html')


def Contact(request):
    if request.method == "POST":
        nam = request.POST["name"]
        em = request.POST["email"]
        mess = request.POST["message"]
        data = contact_us(name=nam,Email_address = em, message=mess)
        data.save()     
        return HttpResponse ("Data saved successfully!")
    return render(request,'contact.html')


# def subscribe_us(request):   
#     if request.method == "POST":
#         e = request.POST["email"]
#         print(e)
#         d = subscribe_us(email=e)
#         d.save()
#         return HttpResponse("subscribed sucessfully")
#     return render(request,'category.hmtl')

def index(request):
    latest = Poster.objects.order_by('-timestamp')[:3]
    posts = Poster.objects.all()
    # paginator = Paginator(Poster,4)
    # page = request.GET.get('page')
    # print(page)
    # try:
    #     posts = paginator.get_page(page)
    # except PageNotAnInteger:
    #     posts = paginator.page(1)
    # except EmptyPage:
    #     posts = paginator.page(paginator.num_pages)
    # print(posts)

    context = {'late':latest,'posts': posts}
    return render(request,'index.html',context)

def single_us(request,slug):
    posts = Poster.objects.filter(slug=slug)
    nextpost = Poster.objects.filter().order_by('slug').first()
    prevpost = Poster.objects.filter().order_by('slug').last()

    post = Poster.objects.filter(slug=slug)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST or None)
        if form.is_valid():
            form.instance.post = Poster.objects.get(slug=slug)
            form.instance.user = request.user
            form.save()
            return HttpResponse("comment saved successfully")
    
    context = {'posts': posts,'nextpost':nextpost,'prevpost':prevpost,'form':form}
    return render(request,'single.html',context)



def Signup_view(request):
    form = SignUpForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password1")
        password2 = form.cleaned_data.get("password2")
        try:
            user = User.objects.create_user(username, email, password)
            return HttpResponseRedirect('login')

        except:
            user = None
        else:
            request.session['signup_error'] = 1 
    return render(request, "Signup.html", {"form": form})


def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect('/')
        else:
            request.session['invalid_user'] = 1
    return render(request, "login.html", {"form": form})

def user_logout(request):
    logout(request)
    return redirect("index")

def search(request):
    if request.method == "GET":
        search = request.GET.get('search')
        post = Poster.objects.filter(title__iexact=search)
        return render(request,'search.html',{'post':post})

        