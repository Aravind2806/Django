from django.shortcuts import render
from django.http import HttpResponse
from .models import department,doctors
from .forms import BookingForm
# Create your views here.
def index(request):

   
   
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')

def booking(request):
    
    if request.method=='POST':
        details=BookingForm()
        if details.is_valid():
            details.save()
        return render(request,'confirmation.html',)       
    
    form=BookingForm()
    dict_form={
        'forms' :form
    }
    return render(request,'booking.html',dict_form)

def doctor(request):
    doc=doctors.objects.all()
    return render(request,'doctors.html',{'doctors':doc})

def contact(request):
    return render(request,'contact.html')

def departments(request):
    dep=department.objects.all()
    return render(request,'departments.html',{'dept':dep})
