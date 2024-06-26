from django.shortcuts import render, redirect
from .models import data
# Create your views here.

def index(request):
    return render(request, 'aerial/index.html')

def about(request):
    return render(request, 'aerial/about.html')

def features(request):
    return render(request, 'aerial/features.html')

def price(request):
    return render(request, 'aerial/price.html')

def contact(request):
    return render(request, 'aerial/contact.html')

def create(request):
    if request.method == "POST":
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        email = request.POST.get('uemail')
        mobile_no = request.POST.get('mn')

        ud = data(first_name=first_name,last_name=last_name,email=email,mobile_no=mobile_no)
        ud.save()

        return redirect("create")
    
    return render(request, 'aerial/create.html')

def retrieve(request):
    ud = data.objects.all()
    return render(request, 'aerial/retrieve.html', {'ud':ud})

def update(request, did):
     if request.method == 'POST':
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        email = request.POST.get('uemail')
        mobile_no = request.POST.get('mn')
        ud = data.objects.get(id=did)
        ud = data(id=did,first_name=first_name,last_name=last_name,email=email,mobile_no=mobile_no)
        ud.save()

        return redirect('retrieve')
    
     ud = data.objects.get(id=did)
     return render(request, 'aerial/update.html', {'ud':ud})

def delete(request, sid):
    dl = data.objects.get(id=sid)
    dl.delete()
    return redirect('retrieve')