from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.
class Home(View):
    def get(self,request):
        return render(request,"input.html")

class Add(View):
    def get(self,request):
        x = request.GET['t1']
        y = request.GET['t2']
        i = int(x)
        j = int(y)
        op = request.GET["operation"]
        if op == 'add':
            k = i + j
            res = HttpResponse("the sum is : "+str(k))
            return res
        elif op == 'sub':
            k = j - i
            res = HttpResponse("the substaction is : " + str(k))
            return res
        elif op == 'mul':
            k = i * j
            res = HttpResponse("the multiplication is : " + str(k))
            return res
        else:
            k = i % j
            res = HttpResponse("the division is : " + str(k))
            return res
