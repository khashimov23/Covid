from django.urls import path

from .views import *

urlpatterns = [
    path('', client_list, name="client_list"),
    path('<int:id>/', detail, name="detail"),
    path('forma/', new_client, name="forma"),
]
