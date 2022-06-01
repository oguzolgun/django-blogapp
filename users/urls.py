from django.urls import path
from .views import home,login,user_logout

urlpatterns = [

    path('/',home,name='home'),
    path('logout/',user_logout,name='logout'),
    # path('register/',register,name='register'),
    path('login/',login, name='login'),

]
