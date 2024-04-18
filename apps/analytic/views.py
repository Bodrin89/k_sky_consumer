from dateutil.parser import parse
from drf_spectacular.utils import OpenApiParameter, extend_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.analytic.dao import AnalyticDAO
from apps.analytic.permissions import AdminRolePermission
from apps.analytic.serializers import (
    GetAnalyticCategorySerializer,
    GetAnalyticDeltaTimeSerializer,
    GetAnalyticPlacesSerializer,
)
from apps.analytic.tasks import analytic_calculate


class GetGeneralAnalyticView(APIView):
    """View для получения общей аналитики"""

    def get(self, request):
        analytic_calculate()
        analytic_places = AnalyticDAO.get_analytic_places()
        analytic_categories = AnalyticDAO.get_analytic_categories()

        analytic_places = GetAnalyticPlacesSerializer(analytic_places, many=True)
        analytic_categories = GetAnalyticCategorySerializer(analytic_categories, many=True)

        combined_data = {'analytic_places': analytic_places.data, 'analytic_categories': analytic_categories.data}

        return Response(combined_data)


@extend_schema(
    description='получение суммы всех чаевых по периоду только пользователем с ролью "ADMIN"',
    parameters=[
        OpenApiParameter(
            name='start_date',
            location=OpenApiParameter.QUERY,
            description='Начальная дата',
            required=False,
            type=str,
        ),
        OpenApiParameter(
            name='end_date',
            location=OpenApiParameter.QUERY,
            description='Конечная дата',
            required=False,
            type=str,
        ),
    ],
)
class GetAnalyticPlacesView(APIView):
    """View для получения суммы всех чаевых по периоду только пользователем с ролью "ADMIN" """

    serializer_class = GetAnalyticDeltaTimeSerializer
    permission_classes = (
        IsAuthenticated,
        AdminRolePermission,
    )

    def get(self, request):
        start_date = request.query_params.get('start_date')
        end_date = request.query_params.get('end_date')

        if not (start_date and end_date):
            return Response({'error': 'Выберете период'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            start_date = parse(start_date)
            end_date = parse(end_date)
        except ValueError:
            return Response({'error': 'Неверный формат даты'}, status=status.HTTP_400_BAD_REQUEST)

        analytic_total_tips_time = AnalyticDAO.get_delta_times(start_date=start_date, end_date=end_date)

        return Response(analytic_total_tips_time, status=status.HTTP_200_OK)
