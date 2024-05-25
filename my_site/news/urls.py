from django.urls import path
from news import views

urlpatterns = [
    path('', views.ClassBasedIndex.as_view(), name='home'),
    path('category/<int:category_id>/', views.ClassBasedGetCategory.as_view(), name='category'),
    path('news/', views.NewsList.as_view(), name='news'),
    path('news/<int:pk>/', views.NewsDetail.as_view(), name='item'),
    path('redirect/', views.Redirect.as_view(), name='redirect'),
    path('form_example/', views.SimpleForm.as_view(), name='form_example'),
]
