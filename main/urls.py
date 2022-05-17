from django.urls import path
from .views import *

app_name= "main"

urlpatterns = [
    path('', main, name="showmain"),
    path('showfirst/', showfirst, name="showfirst"),
    # firstpage URL 연결하기 with 별명사용
    path('showsecond/', showsecond, name="showsecond"),
    path('posts/', posts, name="posts"),
    path('<int:id>', detail, name="detail"),
    path('new/', new, name="new"),
    path('create/', create, name="create"),
    path('edit/<int:id>', edit, name="edit"),
    path('update/<int:id>', update, name="update"),
    path('delete/<str:id>', delete, name="delete"),
]