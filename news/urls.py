from django.urls import path
from .views import category_api, news_api, region_api

app_name = 'news'

urlpatterns = [
    path('api/category/', category_api, name='category_api'),
    path('api/region/', region_api, name='region_api'),
    path('api/news/', news_api, name='news_api'),
]