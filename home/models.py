from django.db import models
import uuid
import os
# Create your models here.
#this will be the three routes so far 
#folder,file
class Folder(models.Model):
    uid = models.UUIDField(primary_key=True,editable=False,default=uuid.uuid4)
    created_at = models.DateTimeField(auto_now_add=True)
    
#make a path to upload the file lookslie -> alkfjeow;fjlasf/file.txt
def get_upload_path(instance,filename):
    return os.path.join(str(instance.folder.uid),filename)

class Files(models.Model):
    folder = models.ForeignKey(Folder,on_delete=models.CASCADE)
    files = models.FileField(upload_to=get_upload_path)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return str(self.folder)    
    
   




    