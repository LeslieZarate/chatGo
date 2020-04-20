from django.urls import path
from .views import * 

app_name = 'message'

message_list = MessageView.as_view({
    'post' : 'create',
    'get' : 'list'
})

message_detail = MessageView.as_view({
    'get': 'retrieve',
    'put'   : 'update',
    'delete': 'destroy'
})




urlpatterns = [
    path('chat/<int:pk_c>/messages', message_list , name='messages_list'),
    path('chat/<int:pk_c>/messages/<int:pk>', message_detail , name='messages_detail')
]