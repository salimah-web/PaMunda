from django import forms
from .models import Category,Product

choices = Category.objects.all().values_list('name','name')
choice=[]
for i in choices:
    choice.append(i)
class product_form(forms.ModelForm):
    class Meta:
        model= Product
        fields=('username','Product_name','category','measurement_scale','price_per_Scale','Quantity_available','image')
        
        widgets= {
            'username':forms.Select(attrs={'class':'form-control'}),
            'Product_name': forms.TextInput(attrs={'class':'form-control'}),
            'category' : forms.Select(choices=choice, attrs={'class':'form-control'})  ,
            'measurement_scale': forms.TextInput(attrs={'class':'form-control'}),
            'price_per_Scale': forms.NumberInput(attrs={'class':'form-control'}),
            'Quantity_available': forms.NumberInput(attrs={'class':'form-control'})
            
                    }


class edit_form(forms.ModelForm):
    class Meta:
        model= Product
        fields=('Product_name','category','measurement_scale','price_per_Scale','Quantity_available','image')
        
        widgets= {
            'Product_name': forms.TextInput(attrs={'class':'form-control'}),
            'category' : forms.Select(choices=choice, attrs={'class':'form-control'})  ,
            'measurement_scale': forms.TextInput(attrs={'class':'form-control'}),
            'price_per_Scale': forms.NumberInput(attrs={'class':'form-control'}),
            'Quantity_available': forms.NumberInput(attrs={'class':'form-control'})
            
                    }