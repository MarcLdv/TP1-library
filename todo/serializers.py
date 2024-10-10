from rest_framework import serializers
from .models import Book, User, UserBook, Loan, Reservation

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['bookId', 'title', 'author', 'status']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['userId', 'name']


class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = ['loanDate', 'returnDate', 'user', 'book']


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ['reservationId', 'reservationDate', 'user', 'book']
