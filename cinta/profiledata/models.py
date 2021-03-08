from django.db import models

class portfolio(models.Model):
    Name = models.CharField(max_length=50)
    Age = models.IntegerField(default=0)
    Images = models.ImageField(upload_to="profiledata/images", default="")
    Skills = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.Name


class skills(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class user_skills(models.Model):
    user_id = models.IntegerField(default=0)
    skill_id = models.IntegerField(default=0)

    def __str__(self):
        return self.skill_id
     