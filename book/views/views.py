from django import forms
from django.db.models.fields import BooleanField
from book.models import book
from django.shortcuts import redirect, render
from django.shortcuts import HttpResponse
from datetime import date
from book_stall.settings import EMAIL_HOST_USER
from book.forms import forms
from django.core.mail import send_mail
from django.conf import settings
from book.forms import *

class subscribe(forms.Form):
    Email=forms.CharField(max_length=100)

    def __str__(self):
        return self.Email
# Create your views here.
def homepage(request):
    sub = subscribe(request.POST)
    if request.method == "POST":
        data=request.POST
        if not data.get("id"):
            if data["ispub"]== "No":
                book.objects.create(name=data["nm"],
                qty=data["qty"],
                price=data["price"],
                is_publish=False)
                # if request.method == 'POST':
                #     sub =subscribe(request.POST)
                #     recipient_list = str(sub['Email'].value()).strip()
                #     message1="Book successfully added"
                #     subject1="Book Added"
                #     send_mail(subject=subject1,message=message1,from_email=EMAIL_HOST_USER,recipient_list=["vipulraut37@gmail.com"], fail_silently = False)
                # return render(request,template_name="homepage.html")
            else:
                book.objects.create(name=data["nm"],
                qty=data["qty"],
                price=data["price"],
                is_publish=True,
                publish_date=date.today())
                # message="Book successfully added",data
                # subject="Book Added",
                # send_mail(subject,message, EMAIL_HOST_USER,recipient_list=["vipulraut38@gmail.com"], fail_silently = False)
                
        else:
            bid=data.get("id")
            book_obj=book.objects.get(id=bid)
            book_obj.name=data["nm"]
            book_obj.qty=data["qty"]
            book_obj.price=data["price"]
            if data["ispub"]=='Yes':
                if book_obj.is_publish:
                    pass
                else :
                    book_obj.is_publish = True 
                    book_obj.publish_date= date.today()
            elif data["ispub"]== 'No':
                if book_obj.is_publish == True:
                    pass
            book_obj.save()
            # message="Book successfully updated",data
            # subject="Book Updated",
            # send_mail(subject,message, EMAIL_HOST_USER,recipient_list=["vipulraut38@gmail.com"], fail_silently = False)
            
            
        return redirect("home")   
        
       
    else:
        return render(request,template_name="homepage.html")
    

    


def show_book(request):
    all_books=book.objects.all()
    return render(request,template_name="stock.html", context={"stock":all_books})

def hard_delete_book(request,id):
    book.objects.get(id=id).delete()
    return redirect('stock')

def edit_book(request,id):
    book_obj=book.objects.get(id=id)
    return render(request,template_name="homepage.html",context={"single_book":book_obj})

def soft_delete_book(request,id):
    book_obj=book.objects.get(id=id)
    book_obj.is_deleted= "1"
    book_obj.save()
    return redirect('stock')

def active_book(request):
    # active_books=book.objects.filter(is_deleted=0)
    active_books=book.active_books.all()
    return render(request,template_name="stock.html", context={"stock":active_books})
    
def inactive_book(request):
    # inactive_books=book.objects.filter(is_deleted=1)
    inactive_books=book.inactive_books.all()
    return render(request,template_name="stock.html", context={"stock":inactive_books,"book_status":"inactive"})

def restore_book(request,id):
    res_book=book.objects.get(id=id)
    res_book.is_deleted="0"
    res_book.save()
    return redirect('stock')

def test_function(request):
    """added a dogstring"""
    pass
