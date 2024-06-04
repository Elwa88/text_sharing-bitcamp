from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Text
from .forms import Textform

# Create your views here.
def index(request):
    texts = Text.objects.all()
    return render(request,'index.html',{'texts':texts})

def add_text(request):
    if request.method == 'POST':
        form = Textform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            return HttpResponse('n0')
    else:
        form = Textform()
        return render(request,'add_text.html',{'form':form})
    
def edit_text(request,id):
    text = Text.objects.get(pk=id)
    if request.method == 'POST':
        form = Textform(request.POST, request.FILES, instance=text)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            return HttpResponse('nein')
    else:
        form=Textform(instance=text)
        return render(request,'edit_text.html',{'form':form})

def display_text(request,id):
    text = Text.objects.get(pk=id)
    return render(request,'display_text.html',{'text':text})