from django.contrib import admin
from .models import portfolio,user_skills,skills

admin.site.register(portfolio)
admin.site.register(skills)
admin.site.register(user_skills)

