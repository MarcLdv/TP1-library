# services.py
from .models import Book, Loan
from datetime import date

def borrow_book(user, book_id):
    book = Book.objects.get(bookId=book_id)
    
    if book.status != "Available":
        raise ValueError("Le livre n'est pas disponible.")
    
    # Créer un emprunt sans utilisateur si user est None
    loan = Loan.objects.create(user=user, book=book, loanDate=date.today(), returnDate=None)
    
    # Mettre à jour le statut du livre
    book.status = "Unavailable"
    book.save()
    
    return loan



def return_book(loan_id):
    loan = Loan.objects.get(loanId=loan_id)
    book = loan.book
    
    # Mettre à jour le statut du livre
    book.status = "Available"
    book.save()
    
    # Supprimer ou marquer l'emprunt comme terminé
    loan.returnDate = date.today()
    loan.save()
    
    return loan
