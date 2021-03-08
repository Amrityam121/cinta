from django.shortcuts import render
from django.http import HttpResponse
from .models import portfolio,skills,user_skills
from uploader.models import uploader 
from django.http import HttpResponse
def index(request):  
    alldata = portfolio.objects.all()
    allskills=skills.objects.all()  
    try:
       alluploader_data=[]
       alluploader_data = uploader.objects.all()

       if alluploader_data:
           alluploader_data=alluploader_data[0]

       Id=alldata[0].id

      
       user_skills_ids=[]
       user_skills_ids=user_skills.objects.filter(user_id=Id).values_list('skill_id', flat=True)
       print("-------------------------",user_skills_ids);
       #user_skills_ids=portfolio.objects.filter(id= 2).values_list('Skills', flat=True)
       
       user_skills_ids=list(user_skills_ids)
       
    except:
        alluploader_data=0
        
   
    return render(request,'profiledata/index.html', {'alldata': alldata,'alluploader_data': alluploader_data,'skills':allskills,'user_skills_ids':user_skills_ids})





def save(request):
   
    if request.method == "POST": 
         print(request.POST)
         Id=request.POST['id']
         print(Id);
         name=request.POST['name']
         age=request.POST['age']
         skills=request.POST.getlist("skills[]")
         userModal=portfolio.objects.get(id=Id)
         userModal.Name=name
         userModal.Age=age
         #userModal.Skills = skills
         userModal.save()
         
         user_skills.objects.filter(user_id=Id).delete()

        
         for skill in skills:
          user_skill_model=user_skills(user_id=Id,skill_id=skill)
          user_skill_model.save(force_insert=True)

       
       

    return HttpResponse("{'result': 'IS_PASS'}", content_type="application/json") 


   
