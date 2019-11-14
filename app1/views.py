from django.shortcuts import render
from .models import Sample

# Create your views here.
def index(request):
    return render(request,"index.html")


def saveDtails(request):
    idno=request.POST.get("t1")
    name=request.POST.get("t2")
    Sample(idno=idno,name=name).save()
    return index(request)


def display(request):
    return render(request,"display.html",{"data":Sample.objects.all()})


def update(request):
    udt=request.POST.get("udt")
    data=Sample.objects.filter(idno=udt)
    return render(request,"update.html",{"data1":data})


def delete(request):
    dell=request.POST.get("dell")
    Sample.objects.get(idno=dell).delete()
    return display(request)


def odelete(request):
    id=request.GET.get("i")
    Sample.objects.filter(idno=id).delete()
    return display(request)