from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, UserViewSet, LoanViewSet, ReservationViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'users', UserViewSet)
router.register(r'loans', LoanViewSet)
router.register(r'reservations', ReservationViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
