from django.urls import path
from .views import about,index,service,team,why


urlpatterns = [
    path('',about,name='about'),
    path('index',index,name='index'),
    path('service',service,name='service'),
    path('team',team,name='team'),
    path('why',why,name='why'),
]
