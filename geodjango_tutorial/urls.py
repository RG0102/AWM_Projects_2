from django.urls import path
from world import views 
from django.contrib import admin

urlpatterns = [         
    path('admin/', admin.site.urls),
    path('map/', views.map_view, name="map"),
]
