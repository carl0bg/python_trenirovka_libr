#Определение схемы URL для пользователей
from django.urls import path, include #для включения аутентификационных URL-адресов по умолчанию
from . import views #необходим так как мы пишем собственное представление для страницы регрессии

app_name = 'users'
urlpatterns = [
    #Включить URL авторизации по умолчанию
    path('', include('django.contrib.auth.urls')),
    #Страница регистрации
    path('register/', views.register, name='register'),
]