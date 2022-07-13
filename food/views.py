from msilib.schema import ListView
from multiprocessing import context
from pyexpat import model
import re
from statistics import mode
#from typing_extensions import Required

from django.http import HttpResponse
from django.shortcuts import redirect, render
from pkg_resources import require


from food.forms import ItemForm
from .models import Item
from django.template import loader

from django.views.generic.list import ListView
#To use inbuilt detail view we import the following package
from django.views.generic.detail import DetailView
#Login required decorator
from django.contrib.auth.decorators import login_required


#Importing CreateView

from django.views.generic.edit import CreateView

# Create your views here.

'''def index(request):
    item_list=Item.objects.all()

    template=loader.get_template('food/index.html')

    context={
      'item_list':item_list,
    }


    HttpResponse(template.render(context,request))
    item_list=Item.objects.all()
    context={
      'item_list':item_list,
    }
    return render(request,'food/index.html',context)'''


class IndexClassView(ListView):
  model=Item;
  template_name='food/index.html'
  context_object_name='item_list'

'''def details(request,item_id):
    #to get data belonging to particular id
    item=Item.objects.get(pk=item_id)

    context={
        'item':item,
    }

    return render(request,'food/detail.html',context)'''

#Creating alternate of functional detail view as a class view.


class DetaislView(DetailView):
  #Here write the model name which will use
  model=Item
  #Here mention the template name too which will use for rendering
  template_name='food/detail.html'
  #Now our class view is ready to use.

  

def item(requet):
    return HttpResponse('This is item view')


@login_required
def create_item(request):
  form=ItemForm(request.POST or None)

  if form.is_valid():
      form.save()
      return redirect('food:index')
  return render(request,'food/item-form.html',{'form':form}) 

#We are creating class view for create_item view



# @login_required
class CreateItem(CreateView):
   model=Item
   fields=['item_name','item_desc','item_price','item_image']
   template_name='food/item-form.html'

   #Validate the form
   def form_valid(self,form):
    form.instance.user_name=self.request.user
    return super().form_valid(form)

def update_item(request,id):
  item=Item.objects.get(id=id)
  form=ItemForm(request.POST or None , instance=item)

  if form.is_valid():
    form.save()
    return redirect('food:index')

  return render(request,'food/item-form.html',{'form':form,'item':item})  


def item_delete(request,id):
  item=Item.objects.get(id=id)

  if request.method=='POST':
    item.delete()
    return redirect('food:index')

  return render(request,'food/item-delete.html',{'item':item})  

