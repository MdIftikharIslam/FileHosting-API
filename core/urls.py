from django.urls import path
from .views import *

urlpatterns = [
    path('file-upload/', FileHandleView.as_view()),
    path('folder/download-view/<str:id>/', FolderSingleView.as_view())
]
