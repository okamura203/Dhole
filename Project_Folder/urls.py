from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('invoice.urls')),
    path('', include('App_Folder.urls')),
    path('Home_Folder', include('Home_Folder.urls')),

]