from django.db import models

class Book(models.Model):
    bookId = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    status = models.CharField(max_length=50, default="Available")

    def __str__(self):
        return f"{self.title} by {self.author}"
    
class User(models.Model):
    userId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    booksList = models.ManyToManyField('Book', through='UserBook')

    def __str__(self):
        return self.name
    
class UserBook(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    added_date = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'book') 

    def __str__(self):
        return f"{self.user.name} added {self.book.title} to their list"
    
class Loan(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)  
    
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    loanDate = models.DateField()
    returnDate = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.name} borrowed {self.book.title}"
    
class Reservation(models.Model):
    reservationId = models.AutoField(primary_key=True)
    reservationDate = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.name} reserved {self.book.title}"
    