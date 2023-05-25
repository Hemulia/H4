from django.urls import path
from .views import *

urlpatterns = [
    path('', ItemListView.as_view()),
    path('item/<int:pk>', ItemUpdateView.as_view()),
    path('item/new', ItemCreateView.as_view()),
    path('item/<int:pk>/delete', ItemDeleteView.as_view()),
    path('brand/', BrandListView.as_view()), 
    path('brand/<int:pk>', BrandUpdateView.as_view()),
    path('brand/new/', BrandCreateView.as_view(), name='brand_new'),
    path('brand/<int:pk>/delete', BrandDeleteView.as_view()),
]
