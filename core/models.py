from django.db import models
from django.contrib.auth.models import User
import os
import uuid

# generates a random folder
def get_file_path(instance, filename):
    return os.path.join(str(instance.folder.id), filename)

class Folder(models.Model):
    id = models.CharField(max_length=255, primary_key=True, blank=True)
    name = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def save(self, *args, **kwargs):
        if len(self.id) == 0:
            self.id = uuid.uuid4()
        return super(Folder, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return str(self.id)

class File(models.Model):
    id = models.CharField(max_length=200, primary_key=True, blank=True)
    file = models.FileField(upload_to=get_file_path)
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.folder)
    
    def save(self, *args, **kwargs):
        if len(self.id) == 0:
            self.id = uuid.uuid4()
        return super(File, self).save(*args, **kwargs)
    