from django.shortcuts import render

# Create your views here.
def wish(request):
    d={'name':'sai shankar','age':24}
    return render(request,'wish.html',context=d)

def well(request):
    d={'name':'sai shankar Vemula'}
    return render(request,'well.html',context=d)