from django.shortcuts import render,redirect
from .form import Imageform
from .models import uploader
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.core.cache import cache
import requests
# Create your views here.
# @csrf_exempt 
# def uploader_index(request):
#     if request.method == "POST":
#         name = request.POST['username']
#         age = request.POST['age']
#         skills = request.POST['skills']
#         pic1 = request.POST['pic1']
#         pic2 = request.POST['pic2']
#         print("pic1 = ", pic1)
#         resData = {
#             "name": name,
#             "age": age,
#             "skills": skills
#         }
#         return JsonResponse(resData)
#     else:
#         return render(request, 'uploader/uploadProfile.html')
    


def Myuploader_index(request):
    if request.method == "POST":    
        form = Imageform(data=request.POST,files= request.FILES)
        alldbdata = uploader.objects.all()
        print(alldbdata,'.....',len(alldbdata))
        if len(alldbdata) > 1:
            print(alldbdata)
            print(len(alldbdata))
            messages.error(request, 'Max limit of upload has reached')

            return redirect('Myuploader_index')
            # return render(request, 'uploader/uploadpage.html',{"db_status": True})
                    
        else: 
            form.is_valid()
            try:
               form.save()
            except:
                 messages.error(request, 'dimesion issues')
                 return redirect('Myuploader_index')
            obj =form.instance
            messages.success(request, 'your response has been recorded')
            return redirect('Myuploader_index')
            #    return render(request,'uploader/uploadpage.html',{"obj":obj ,'status': False,'db_status': False}) 
    else:
        form =Imageform()
        img =uploader.objects.all()
        response = 'response'
        data = {'request':request,'response':response }
        db_cache = cache.get_or_set('req_res', 'data', 20)
    return render(request, 'uploader/uploadpage.html',{"img":img,"form":form})

    
def destroy_photo(request,id):
    data_tobe_deleted=uploader.objects.filter(id =id).delete()
    
    return redirect("/myupload")  
   
    
    