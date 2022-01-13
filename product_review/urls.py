from django.contrib import admin
from django.urls import re_path
from django.conf.urls import include
from reviews.views import ProductVeiwSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'product', ProductVeiwSet, basename='Product')

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^', include(router.urls)),

]
