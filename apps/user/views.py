from rest_framework.generics import CreateAPIView

from apps.user.models import UserModel
from apps.user.serializers import CreateUserSerializer


class CreateUserView(CreateAPIView):
    """Создание пользователя"""

    serializer_class = CreateUserSerializer
    queryset = UserModel.objects.all()
