"""
URL configuration for chatbot_jv project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from .callbacks import *
from django.urls import path
from django.chatbot.views import web_hook
from bearer_auth.views import ObtainToken
from bearer_auth.authentication import BearerTokenAuth
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rest_framework import exceptions


@csrf_exempt
def web_hook_authenticate(request, *args, **kwargs):
    print(request.body)
    try:
        request.user, _ = BearerTokenAuth().authenticate(request, *args, **kwargs)
    except exceptions.AuthenticationFailed as error:
        return JsonResponse({
        "status": "Error",
        "error": str(error) ,
        "ErrorType": "AuthenticationFailed" 
        })
    except Exception:
        return JsonResponse({
            "status": "Error",
            "error": "Internal server error",
            "ErrorType": "InternalServerError"
        })
    return web_hook(request, *args, **kwargs)


urlpatterns = [
    path('admin/', admin.site.urls),
    path("webhook/", web_hook_authenticate, name="webhook"),
    path('auth/token', ObtainToken.as_view()),
]
