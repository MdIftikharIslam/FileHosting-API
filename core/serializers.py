from rest_framework import serializers
from .models import *
import shutil

#---------------------------------------------------
# File Handle Upload Serializer Starts

class FileHandleSerializer(serializers.Serializer):
    file = serializers.ListField(
        child=serializers.FileField()
    )
    folder = serializers.CharField(required=False)
    folder_name = serializers.CharField(max_length=200, required=True)

    def zip_files(self, folder):
        return shutil.make_archive(f"media/zip/{folder}", "zip", f"media/{folder}")

    def create(self, validated_data):
        user = self.context.get('request').user
        folder = Folder.objects.create(name=validated_data['folder_name'], user=user)
        files = validated_data['file']
        for f in files:
            File.objects.create(file=f, folder=folder)
        
        self.zip_files(folder.id)
        return {"file":[], "folder":str(folder.id), "folder_name":validated_data['folder_name']}

# File upload serializer ends here
#---------------------------------------------------

# Serializer for list and single view of folder for downlaod views
class FolderGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Folder
        fields = "__all__"