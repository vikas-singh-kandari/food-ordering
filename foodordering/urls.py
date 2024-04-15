
from django.contrib import admin
from django.urls import path
from foodordering import views
from partner.views import *
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name="homepage"),
    path('shoplist', views.shoplist,name="shoplist"),
    path('becomepart', views.becomepart, name = "becomepart"),
    path('signup', views.signup,name="signup" ),
    path('addshop/', addshop,name="addshop"),
    path('delete_shop/<id>/',delete_shop, name="delete_shop"),
    
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    
urlpatterns += staticfiles_urlpatterns()
