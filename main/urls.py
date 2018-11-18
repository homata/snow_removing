from django.urls import include, path
from . import views
from django.views.generic.base import RedirectView

# アプリケーションの名前空間
# https://docs.djangoproject.com/ja/2.0/intro/tutorial03/
app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
]
