from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(['GET'])
def ApiRoutes(request):

    data = {
        "urls":{
            "Login-Route":"auth/login/",
            "Register-Route":"auth/register/",
            "File-Upload-Route":"core/file-upload/",
            "File-Download-Route":"core/folder/download-view/<str:id>/"
        },
        "Request-Methods":{
            "Login-Route":"POST",
            "Register-Route":"POST",
            "File-Upload-Route":"POST",
            "File-Download-Route":"GET",
        }
    }
    return Response({
        'status':status.HTTP_200_OK,
        'data':data
    })