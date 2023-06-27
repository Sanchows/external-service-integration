from django.urls import path
from apps.core.views import get_employes_list_view


urlpatterns = [
    path('team/get_employees/', get_employes_list_view, name='external-get-employes-list'),
]
