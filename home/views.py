from django.shortcuts import render,HttpResponse
from django.contrib.auth.decorators import login_required


# Create your views here.
@ login_required
def homepage(request):
    return render(request,"home/base.html")

def index(request):
    return  render(request,"home/index.html")