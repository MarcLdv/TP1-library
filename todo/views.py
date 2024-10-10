from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Book, User, Loan, Reservation
from .serializers import BookSerializer, UserSerializer, LoanSerializer, ReservationSerializer
from .services import borrow_book, return_book

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class LoanViewSet(viewsets.ModelViewSet):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer

    def create(self, request, *args, **kwargs):
        book_id = request.data.get('book')
        user = None  # Si vous ne voulez pas utiliser l'utilisateur connecté
        
        try:
            loan = borrow_book(user, book_id)
            serializer = self.get_serializer(loan)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": "Une erreur est survenue."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    