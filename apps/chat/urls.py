from django.urls import path
from .views import * 


app_name = 'chat'

chat_list = ChatView.as_view({
    'post' : 'create',
    'get' : 'list'
})

chat_detail = ChatView.as_view({
    'get': 'retrieve',
    'put'   : 'update',
    'delete': 'destroy'
})




urlpatterns = [
    path('chat', PageChatView.as_view(), name='page_chat'),
    path('contact/<int:pk_c>/chats', chat_list , name='chats'),
    path('contact/<int:pk_c>/chats/<int:pk>', chat_list , name='chats')
]