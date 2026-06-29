from django.shortcuts import render,redirect
from .forms import *

# Create your views here.
def index(request):
    return render(request,'index.html')

def signup(request):
    if request.method=='POST':
        newReq=SignupForm(request.POST)
        if newReq.is_valid():
            newReq.save()
            print("Signup Successfully!")
            return redirect('/')
        else:
            print(newReq.errors)
    return render(request,'signup.html')