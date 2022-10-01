from django.shortcuts import render,HttpResponse
from .models import bank_dtl
from .forms import bank_form

# Create your views here.
def bank_views(request):
    if request.method=='POST':
        form==bank_form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Registration sucessfull")
        else:
            return HttpResponse("Failed response")



    else:
        form=bank_form()
        return render(request,'register.html',{'form':form})
