
from django.urls import path
from app import views


urlpatterns = [
    path('',views.index,name="index"),
    path('about',views.about,name="about"),
    path('create/',views.create,name="create"),
    path('insert/',views.insertData,name="insertData"),
    path('delete/',views.insertData,name="insertData"),
    path('update/<id>',views.updateData,name="updateData"),
    #path('delete1',views.del)
    #path('delete/<id>',views.deleteData,name="deleteData"),
    path('delete/<id>/', views.deleteData, name='deleteData'),
]