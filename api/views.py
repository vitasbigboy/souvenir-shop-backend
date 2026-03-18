from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def test_user(request):
    """Возвращает тестового пользователя"""
    user_data = {
        'id': 1,
        'username': 'test_user',
        'email': 'test@example.com',
        'first_name': 'Тест',
        'last_name': 'Тестовый'
    }
    return Response(user_data)

@api_view(['GET'])
def ping(request):
    return Response({'message': 'pong'})