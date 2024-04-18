from rest_framework.generics import ListAPIView

from apps.store.models import StoreModel
from apps.store.serialezers import GetAllPlacesSerializer


class GetAllPlacesView(ListAPIView):
    serializer_class = GetAllPlacesSerializer
    queryset = StoreModel.objects.all()
