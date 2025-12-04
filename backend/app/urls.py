from django.contrib import admin
from django.urls import path
from usuarios.views import RegisterView, LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('') Inicio
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/login/', LoginView.as_view(), name='login')
]
