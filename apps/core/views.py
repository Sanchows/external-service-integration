from asgiref.sync import sync_to_async
import requests
from rest_framework.decorators import api_view
from rest_framework.views import Response, status

from apps.core import requests_service
from apps.core.models import APIEndpoint
from apps.core.serializers import EmployesRequestSerializer


@sync_to_async
@api_view(["GET"])
def get_employes_list_view(request):
    external_endpoint = "1c employers"
    queryset = APIEndpoint.objects.filter(title=external_endpoint)
    if not queryset:
        return Response(
            data={"detail": f"There is no an endpoint: {external_endpoint}"},
            status=status.HTTP_400_BAD_REQUEST
        )
    endpoint = queryset.first()

    login = endpoint.authorization.username
    password = endpoint.authorization.password
    params = dict(endpoint.parameters.values_list('name', 'value'))
    club_id = params.get('ClubId')
    if not club_id:
        return Response(
            data={"detail": "There is no a required argument 'ClubId' in DB. Please add it using the admin panel"},
            status=status.HTTP_400_BAD_REQUEST
        )
    try:
        response_from_external_endpoint = requests_service.post_1c(
            uri=endpoint.url,
            login=login,
            password=password,
            club_id=club_id,
        )
    except requests.exceptions.ConnectionError:
        # эндпоинт не рабочий, поэтому самописный ответ отправляю
        response_from_external_endpoint = [
            {
                "id": "123",
                "name": "имя сотрудника",
                "last_name": "(фамилия сотрудника)",
                "phone": "+13453452452",
                "image_url": "http://images.mydomain/photojpg.jpg",
            },
            {
                "id": "12333",
                "name": "имя сотрудника2",
                "phone": "+1343352",
                "image_url": "http://images.mydomain/photojpg123.jpg",
            },
            {
                "id": "41234",
                "name": "имя сотрудника3",
                "phone": "+134335224324",
                "image_url": "http://images.mydomain/photojpg1243234.jpg",
            },
        ]

    serializer = EmployesRequestSerializer(response_from_external_endpoint, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)
