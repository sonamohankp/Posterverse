from django.contrib import messages
from django.shortcuts import render, redirect

from .models import Designers

def des_view(request):
    data = Designers.objects.all()
    return render(request,'admin/des_view.html',{'data':data})



def desinger_approval(request,id):
    data = Designers.objects.get(id=id)
    data.status = True
    data.save()
    return redirect('des_view')

