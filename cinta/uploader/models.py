from django.db import models
from PIL import Image
from django.core.exceptions import ValidationError
# Create your models here.

def validate_image(Images):
       min_height = 300
       min_width = 300
       height = Images.height 
       width = Images.width

       if width < min_width or height < min_height:
        print(width,height)
        print('working')
        raise ValidationError("Height or Width is smaller than what is allowed")

    
class uploader(models.Model):
    caption = models.CharField(max_length=100)
    Images = models.ImageField(upload_to="picdata/%y",validators=[validate_image])


    

    def __str__(self):
        return self.caption