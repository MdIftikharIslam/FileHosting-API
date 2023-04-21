from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import *
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status


#-----------------------------------------------------
# File upload view starts here

class FileHandleView(APIView):
    
    permission_classes = [IsAuthenticated]
    def post(self, request):
        data = request.data
        # print(data)
        context = {
            'request':request
        }
        serializer = FileHandleSerializer(data=data, context=context)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)
        
        return Response({
            'status':200,
            'details':'something went wrong',
            'data':serializer.errors,
            'requst-data':data
        })
    
    def get(self, request):
        user = request.user
        folder_obj = Folder.objects.filter(user=user)
        serializer = FolderGetSerializer(folder_obj, many=True)
        return Response({
            'status':status.HTTP_200_OK,
            'data':serializer.data
        })
    

# File upload view ends here    
#-----------------------------------------------------


# Folder Download View    
class FolderSingleView(APIView):
    def get(self, request, id):
        folder_obj = Folder.objects.get(id=id)
        serializer = FolderGetSerializer(folder_obj, many=False)
        folder_url = serializer.data['id']
        return Response({
            'status':status.HTTP_200_OK,
            'data':serializer.data,
            'download-url':f"http://127.0.0.1:8000/media/zip/{folder_url}.zip"
        })