from django.urls import path 
from .exam_views import ChatView



urlpatterns = [


    # path('', ChatView.as_view(), name='chat_api'),  # Add this default route
    path('chat/', ChatView.as_view(), name='chat_view'),


]
