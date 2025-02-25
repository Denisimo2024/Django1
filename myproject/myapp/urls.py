from django.urls import path
from .views import data_view, test_view, home_view

urlpatterns = [
    path('', home_view, name='home'),
    path('data/', data_view, name='data'),
    path('test/', test_view, name='test'),
]
