from django.urls import path
from aksessuarlar.views import get_info

urlpatterns = [
    path('', get_info)
]