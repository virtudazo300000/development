from django.urls import path
from .views import HelloWorld, Students,  ContactListView

urlpatterns =  [
    path('hello/', HelloWorld.as_view(), name= 'hello_world'),
    path('students/', Students.as_view(), name= 'list_students'),
    path('infocontact/',ContactListView.as_view(), name='contact_new'),
    
    
]
