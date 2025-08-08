# I have created this file-- 
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from service.models import Service
from enquery.models import Enquery 
from image.form import Imageform
from image.models import Image
from django.core.paginator import Paginator , EmptyPage, PageNotAnInteger
def home (request):
     return render(request,'home.html')

def service(request):
    data = Service.objects.all().order_by('id')
    paginator = Paginator(data, 3)
    page = request.GET.get('page')
    final_data= paginator.get_page(page)

    try:
       final_data = paginator.get_page(page)
    except PageNotAnInteger:
        final_data = paginator.get_page(1)
    except EmptyPage:
        final_data = paginator.get_page(paginator.num_pages)

    D = {'data': final_data}
    return render(request, 'service.html', D)
    

def about(request):
     return render(request,'about.html')

def contact(request):
     return render(request,'contact.html')

def saveData(request):
     if request.method == 'POST':
       name = request.POST.get('name')
       email= request.POST.get('email')
       phone = request.POST.get('phone')
       whtasapp_no = request.POST.get('whtasapp_no')
       description= request.POST.get('description')
       image= request.POST.get('image')
       en = Enquery(name= name, email= email, phone= phone,whatsapp_no= whtasapp_no, description= description,image= image) 
       en.save()
     return render(request,'contact.html')


def more(request):
    if request.method == 'POST':
        form = Imageform(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            obj = form.instance  
            return render(request, 'more.html', {'obj': obj})  
    else:
        form = Imageform()  
        img = Image.objects.all()  
    return render(request, 'more.html', {'img': img, 'form': form})



