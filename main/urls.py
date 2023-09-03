from django.urls import path,include
from .views import Hompage,Suras,get_sura,Hompage,Buttons
urlpatterns = [
    path('', Buttons, name='main'),
    path('audios/', Hompage, name='audios'),
    path('suralar/', Suras, name='suralar'),
    path('suras/<str:sura>/', get_sura, name='sura')    
  

]
