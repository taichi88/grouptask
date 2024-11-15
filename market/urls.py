"""
URL configuration for market project.

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
from email.policy import default

from django.contrib import admin
from django.urls import path, include
from rest_framework.schemas import get_schema_view
from drf_yasg import openapi
from drf_yasg.views import get_schema_view as swagger_get_schema_view


#2. ეს იგივე მონაცემები შეიტანე რაც ქემოთ სქმისათვის, თუმცა ამ შემთხვევაში სქემის გენერირებაზე იზრუნებს სვაგერი და ეს იქნება უფრო გამართUლი სტრუქტურით
schema_view = swagger_get_schema_view(openapi.Info(
    title="Nika Gabeskiria API Schema",
    default_version = "1.0.0",
    description="Api განმარტება ჩვენი API market სქემისთვის",

), public=True)



urlpatterns = [
    #1. სქემისათვის ურლ-ის დამატება (ასევე ამისათვის ვაიმპორტე get_schema_view კლასს)
    path("api_schema/", get_schema_view(
        title = "Nika Gabeskiria API Schema",
        description= "Api განმარტება ჩვენი API market სქემისთვის"
    ), name="api_schema"),


    #2. ეს იქნება სვაგერის პეთსი
    path("swagger/", schema_view.with_ui("swagger"), name="swagger"),


    path('admin/', admin.site.urls),
    path('api/cars/', include("car.urls")),
    path('api/user/', include("user.urls"))
]




