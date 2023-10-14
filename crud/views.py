from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth import authenticate, login, logout 
from .forms import UserCreationForm, LoginForm
from django.views.generic.edit import CreateView,UpdateView
from django.contrib.auth.models import User
from django.db.models import Q



def profile_view(request, username):
    u = User.objects.get(username=username)
    posts = Post.objects.all()
    hdata3 = Profile.objects.all()
    conte = {
        'users':u,
        'posts':posts,
        'profile':hdata3,

    }
    return render( request,'userabout.html', context=conte)



class Postcreate(CreateView):
    model = Post
    template_name = "postcreate.html"
    fields ="__all__"
    success_url = '/'

class Post_edit(UpdateView):
    model = Post
    template_name='postedit.html'
    fields='__all__'
    success_url = '/'




def homepage(request):
    q = request.GET.get('q') if request.GET.get('q') !=  None  else '' 
    hdata1 = Category.objects.all()
    hdata2 = Post.objects.filter(
        Q(categ__title__icontains=q)|
        Q(title__icontains=q)
        )
    hdata3 = Profile.objects.all()
    users = User.objects.all().order_by('-id')
    mydata = {
        'data1':hdata1,
        'data2':hdata2,
        'data3':hdata3,
        'q':q,
        'users':users,
    }

    return render(request, 'index.html',context=mydata)

def user_signup(request):
    if request.method == 'POST':

        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'signup.html', {'form': form})

def delete_post(request,id):
    hdata1 = Post.objects.get(id=id)
    hdata1.delete()
    return redirect('/')





def user_login(request):
    problem = []
    if request.method == 'POST':
        problem.append('Hatolik yuz berdi iltimos kodni yoki ismingizni qaytadan tekwirib kirgazing')
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password )
            if user:
                login(request, user)    
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form,'pr':problem})


class User_profile(CreateView):
    model = Profile
    template_name='addprofile.html'
    fields = '__all__'
    success_url = '/'

class Profile_edit(UpdateView):
    model = Profile
    template_name='profile_edit.html'
    fields='__all__'
    success_url = '/'



def user_logout(request):
    logout(request)
    return redirect('login')