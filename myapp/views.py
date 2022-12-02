
from django.http import HttpResponse
from django.shortcuts import render

from .models import Feature

# Create your views here.
def index(request):
    return render(request,'index.html')

def search(request):
        word=request.POST['tex']
        a=Feature(question=word)
        a.save()
        return HttpResponse("Thank you for submitting your question ")
        

def all(request):
    data=Feature.objects.all()
    return render(request,'recent.html',{'value':data})
