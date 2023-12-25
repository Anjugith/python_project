from django.http import HttpResponse
from django.shortcuts import render
from . models import Place
from . models import Workers
# Create your views here.
def demo(request):
    obj=Place.objects.all()
    obj2=Workers.objects.all()
    return render(request,"index.html",{'result':obj,'wresult':obj2})
# def wdemo(request):
#     obj=Workers.objects.all()
#     return render(request,"index.html",{'wresult':obj})
#def demo(request):
  #  name='Operations'
 #   return render(request,'home.html',{'obj':name})
#def operations(request):
    #x=int(request.GET['num1'])
   # y = int(request.GET['num2'])
  #  res1=x+y
 #   res2=x-y
#    res3=x*y
    #res4=x/y
    #return render(request,'result.html',{'result1':res1,'result2':res2,'result3':res3,'result4':res4})