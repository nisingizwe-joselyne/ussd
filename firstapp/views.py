from django.shortcuts import render

# Create your views here.
def welcome(request):
    return render(request,'dash.html')
    
def about(request):
    return render(request,'about.html')