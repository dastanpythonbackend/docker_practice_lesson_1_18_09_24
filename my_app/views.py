from django.shortcuts import get_object_or_404
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, viewsets
from rest_framework.response import Response
from .models import CarBrand
from .serializers import CarBrandSerializer

# Create your views here.


class CarBrandView(generics.ListCreateAPIView):
    queryset = CarBrand.objects.all()
    serializer_class = CarBrandSerializer

    @swagger_auto_schema(
        operation_description='Возвращает список всех машин'
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description='Заполняет модель CarBrand',
        responses={201: openapi.Response('Автомобиль создан', CarBrandSerializer), 400: "Ошибка валидации"},
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'name': openapi.Schema(type=openapi.TYPE_STRING, description='Имя автомобиля'),
                'country': openapi.Schema(type=openapi.TYPE_STRING, description='Страна производителя'),
                'info': openapi.Schema(type=openapi.TYPE_STRING, description='Информация о автомобиле'),
            },
            required=['name', 'country', 'info'],
            example={
                "name": "Toyota Camry 3.5",
                "counry": "Japan",
                "info": "Toyota Camry 3.5"
            }
        )
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class CarViewSet(viewsets.ViewSet):
    @swagger_auto_schema(
        operation_description="Получить детали конкретного автомобиля по ID",
        responses={200: CarBrandSerializer(), 404: "Не найдено"}
    )
    def retrieve(self, request, pk=None):
        car = get_object_or_404(CarBrand, pk=pk)
        serializer = CarBrandSerializer(car)
        return Response(serializer.data)
