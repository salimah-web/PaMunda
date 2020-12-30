
from django.shortcuts import render,redirect,get_object_or_404,HttpResponseRedirect
from django.views.generic import CreateView, ListView, DeleteView,UpdateView
from .models import Product,user_profile, Category
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from .forms import product_form, edit_form
from django.urls import reverse
import stripe
from django.http import JsonResponse
# Create your views here.

stripe.api_key="sk_test_51HzbSCKITam3x3WsWzkv9ogmy4wO2hjDuqhy8vfBL9V5OnATOQHGV2gxVuKYhvRxkEYDD5o2G98o9JqNa1OAkMpy005h5Bpp6D"


def home(request):
    catss=Category.objects.all()
    return render(request, 'home.html',{'food':catss})

class all_product(ListView):
    template_name='product_list.html'
    model=Product


class add_post(CreateView):
    template_name='add_post.html'
    form_class=product_form
    

def trans(request,pk):
    obj=Product.objects.get(id=pk)
    if request.method=='POST':
        name=obj.Product_name
        print(name)
    return render(request, 'order.html',{'obj':obj})

def charge(request):
    amount=5

    if request.method =='POST':
        print(5)
        print('Data:',request.POST)
        customer=stripe.Customer.create(
            email=request.user.email,
            source=request.POST['stripeToken']
        )
        m=int(float(request.POST['price']))
        n=int(request.POST['quantity'])
        stripe.Charge.create(
            customer=customer,
            
            amount=m*n,
            currency="usd",
            description='ass',
            
            )

    return redirect(reverse('success'))

def success_msg(request):
    
    return render(request, 'success.html')



# class add_profile(CreateView):
#     template_name='profile.html'
#     model=user_profile
#     fields='__all__'

class add_category(CreateView):
    template_name='add_category.html'
    model=Category
    fields='__all__'

class update_profile(UpdateView):
    model= user_profile
    template_name='update_profile.html'
    fields='__all__'


def categories(request, cats):
    obj_cat=Product.objects.filter(category=cats)
    catss=Category.objects.filter(name=cats)
    context={
        'obj_cat':obj_cat,
        'cats':cats,
        'catss':catss
    }
    return render(request, 'categories.html',context)

def details(request, pk):
    obj=Product.objects.get(id=pk)
    context={
        'obj':obj
    }
    return render(request, 'details.html', context)

def update(request, pk): 
    obj = get_object_or_404(Product, id = pk) 
    form = edit_form(request.POST or None, instance = obj)
    context ={'form':form} 
      
    if form.is_valid(): 
        form.save() 
        return HttpResponseRedirect("/details/"+ str(obj.pk))  
    return render(request, "update.html", context) 

# class update(UpdateView):
#     form_class=edit_form
#     template_name='update.html'
#     success_url= reverse_lazy('all_product')

def delete(request, pk): 
    obj = get_object_or_404(Product, id=pk) 
    context ={'obj':obj} 
  
  
    if request.method =="POST": 
        obj.delete()  
        return HttpResponseRedirect("/product_list") 
  
    return render(request, "delete.html", context) 

# class delete(DeleteView):
    
#     model= Product
#     template_name='delete.html'
#     success_url= reverse_lazy('homepage')
    
    
