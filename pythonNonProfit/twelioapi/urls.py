from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import NonprofitViewSet, FoundationViewSet, EmailRecordViewSet

router = DefaultRouter()
router.register(r'nonprofits', NonprofitViewSet)
router.register(r'foundations', FoundationViewSet)
router.register(r'emailrecords', EmailRecordViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
