from django.http.response import HttpResponse
from django.shortcuts import render
# Create your views here.
from .forms import subscribe
from django.shortcuts import render
from book_stall.settings import EMAIL_HOST_USER
from . import forms
from django.core.mail import send_mail,EmailMessage
from django.conf import settings


# Create your views here.
#DataFlair #Send Email
def subscribe_email(request):    #Fuction based View
    sub = forms.subscribe()       # here request method is get
    if request.method == 'POST':
        sub = forms.subscribe(request.POST)
        subject = 'Request to Lunch'    
        message = 'Bhook Lagli...Lavr swayampak Kr'
        # recepient= request.POST["email"].strip()
        recepient = str(sub['Email'].value()).strip()
        final_recepient_list= None
        if ";" in recepient:
            final_recepient_list=recepient.split(";")
        else:
            final_recepient_list=[recepient]
        # print(recepient_list)
        if final_recepient_list:
            # send_mail(subject,message, EMAIL_HOST_USER,recipient_list=final_recepient_list, fail_silently = False)
            msg=EmailMessage(subject,message,from_email=EMAIL_HOST_USER,to=final_recepient_list,cc=["vipulraut37@gmail.com"],bcc=["ganbangare143@gmail.com"])
            msg.attach_file("C:\\Users\\Vipul Raut\\OneDrive\\Desktop\\Django and mysql databases connection.txt")
            msg.send(fail_silently=False)
            # msg.message("asdfghjkhgfcdxsz")
            msg.recipients()
            
        return render(request,template_name="success.html",context={'recepient': recepient})
    return render(request,template_name='index.html',context={'form':sub})
    # return HttpResponse("Hi") 