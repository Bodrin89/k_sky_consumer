from django.urls import path

from apps.analytic.views import GetAnalyticPlacesView, GetGeneralAnalyticView

urlpatterns = [
    path('', GetGeneralAnalyticView.as_view(), name='get_general_analytic'),
    path('delta-times', GetAnalyticPlacesView.as_view(), name='get_delta_times'),
]
