from rest_framework.routers import DefaultRouter
from .views import ContactUsViewSet
from django.urls import path, include

router = DefaultRouter()


router.register('contact_us', ContactUsViewSet)

urlpatterns=[

    path('', include(router.urls)),
]