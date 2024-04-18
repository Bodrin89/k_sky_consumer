from django.urls import path

from apps.store.views import GetAllPlacesView

urlpatterns = [
    path('', GetAllPlacesView.as_view(), name='get_all_places'),
]
