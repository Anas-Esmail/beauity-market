from ast import Return
from multiprocessing import context
from re import template
from django.shortcuts import render
from makeup.models import *
# Create your views here.
def index(request):
    brandss=brands.objects.all()
    productss=products.objects.all()
    context={"brnad":brandss,"products":productss}
    template='makeup/index.html'
    return render(request,template,context)

def brandlist(request):
    brandss=brands.objects.all()
    context={"brnad":brandss}
    template='makeup/brandlist.html'
    return render(request,template,context)


def branddetails(request,username='defultuser'):
    brandss=brands.objects.all().filter(name=username)
    context={"brands":brandss}
    template='makeup/branddetails.html'
    return render(request,template,context)


def productdetail(request,username='defultuser'):
    productss=products.objects.all().filter(name=username)
    context={"products":productss}
    template='makeup/productdetail.html'
    return render(request,template,context)


def productlist(request):
    productss=products.objects.all()
    context={"products":productss}
    template='makeup/productlist.html'
    return render(request,template,context)
