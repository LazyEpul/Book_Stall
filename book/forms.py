from django import forms

class subscribe(forms.Form):
    Email=forms.CharField(max_length=100)
    # Name= forms.CharField(max_length=100)


    def __str__(self):
        return self.Email