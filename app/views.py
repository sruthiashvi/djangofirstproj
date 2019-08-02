from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse
from datetime import datetime
from .models import TodosModel #new
from django.contrib.auth.forms import UserCreationForm #new
from django.contrib.auth.models import auth
from .forms import LoginForm
from .forms import TodosForm
from django.views.generic import ListView,CreateView,DetailView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.core.paginator import Paginator

# Create your views here.
#def home(request):
    #return HttpResponse("<h1>Homepage</h1>") 
    #serverTime=datetime.now()
    #return render(request,"home.html",{'currentTime':serverTime})
   #todos=TodosModel.objects.all()
    #return render(request,"home.html",{'todos':todos})
def about(request):
    #return HttpResponse("<h1>About page</h1>")
    return render(request,"about.html")
def add(request):
     #n1=int(request.GET["a"])
     #n2=int(request.GET["b"])
     n1=int(request.POST["a"])
     n2=int(request.POST["b"])
     result=n1+n2
     return render(request,"add.html",{"result":result})
def register(request):
     form=UserCreationForm()
     if request.method=="POST":
          form=UserCreationForm(request.POST) 
          if form.is_valid():
               form.save()
               username=form.cleaned_data.get('username')
               messages.success(request,"Account created for " + username)
               return redirect('/')
     return render(request,'register.html',{'form':form})
def login(request):
    #return HttpResponse("<h1>About page</h1>")
     if request.method=="POST":
          username=request.POST["username"]
          password=request.POST["password"]
          #if auth success,auth.authenticate() returns user object
          user=auth.authenticate(username=username,password=password)

          if user is not None:
               auth.login(request,user) #give permission to login
               return redirect("/")
          else:
               messages.error(request,"Invalid")
               return redirect("login")
     else:
          form=LoginForm()
          return render(request,"login.html",{'form':form})
def logout(request):
    #return HttpResponse("<h1>About page</h1>")
    auth.logout(request)
    return render(request,"logout.html")
class TodosListView(ListView):
     model=TodosModel
     template_name="home.html"
     context_object_name="todos"
     ordering=["name"]
     paginate_by=2 #no of todos in page
class TodosCreateView(LoginRequiredMixin,CreateView):
     model=TodosModel
     template_name="todosmodel_form.html"
     fields=["name","completed"]
class TodosDetailView(DetailView):
     model=TodosModel
     template_name="tododetail.html"
class TodosUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
     model=TodosModel
     template_name='todosmodel_form.html'
     fields=["name","completed"]
     def form_valid(self,form): #method to assign username to author for updating author name in todo
          form.instance.owner=self.request.username
          return super().form_valid(form)
     def test_func(self): #fn to permit editing
          todo=self.get_object()
          #return True
          if self.request.user==todo.owner:
               return True
          return False

class TodosDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
     model=TodosModel
     template_name='delete.html'
     success_url='/'
     def test_func(self):
          post=self.get_object()
          #return True
          if self.request.user==post.owner:
               return True
          return False