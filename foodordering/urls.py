
from django.contrib import admin
from django.urls import path
from foodordering import views
 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name="homepage"),
    path('shoplist', views.shoplist,name="shoplist"),
    path('becomepart', views.becomepart, name = "becomepart"),
    path('signup', views.signup,name="signup" ),
    path('addshop', views.addshop,name="addshop")
    
] 
