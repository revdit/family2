from django.shortcuts import render

# Create your views here.
def relation_home(request):
    return render(request,'relation/home.html')

def relation_page1(request):
    return render(request,'relation/page1.html')

def relation_page2(request):
    return render(request,'relation/page2.html')

def relation_page3(request):
    return render(request,'relation/page3.html')