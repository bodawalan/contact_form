from django.shortcuts import render,redirect
from .models import user
from .forms import detail_form
from django.http import HttpResponseRedirect


def form_view(request):

    if request.method=="POST":
        form = detail_form(request.POST)

        if form.is_valid():
            first_name=request.POST.get('first_name','')
            last_name = request.POST.get('last_name', '')
            address = request.POST.get('address', '')
            city = request.POST.get('city','')
            state = request.POST.get('state','')
            zipcode = request.POST.get('zipcode','')
            email = request.POST.get('email','')
            phone_number = request.POST.get('phone_number','')
            context={"form_obj":user(first_name=first_name,last_name=last_name,address=address,city=city,state=state,zipcode=zipcode,email=email,phone_number=phone_number)}

            context.save()
           # return HttpResponseRedirect('/')
            return render(request,'form.html', context)
        else:
            context = {"form":detail_form()}
            return render(request,'form.html', context)

def showform(request):
    context = {"user_form":user.objects.all()}
    return render(request,'show_form.html',context)



