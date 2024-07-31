from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class userDetails(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    college_name =models.CharField(max_length=30)
    phone=models.IntegerField()
    roll_no=models.IntegerField()
    register_id = models.CharField(max_length=20)
    department=models.CharField(max_length=10)


class Library_Book_Details(models.Model):
    book_name=models.CharField(max_length=50)
    book_image = models.ImageField(upload_to='images/')
    Author = models.CharField(max_length=50)
    book_id=models.IntegerField()
    description =models.CharField(max_length=500)
    available_copies = models.IntegerField()

    def __str__(self):
        return self.book_name


# 121 connection: one person have connection with one column. one to one connectionil foreign key use cheyyan pattula.
# 1 to many connection: one person have connection with multiple connection.


class BookRequest(models.Model):
    user = models.ForeignKey(userDetails,on_delete=models.CASCADE)
    book = models.ForeignKey(Library_Book_Details,on_delete=models.CASCADE)
    request_date =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"request by  {self.user.user.username} for {self.book.book_name}"


class Accepted_books_model(models.Model): # this model is not necessary
    # book_details = models.ForeignKey(BookRequest,on_delete=models.CASCADE)
    book_name = models.CharField(max_length=50)
    book_image = models.ImageField(upload_to='images/')
    Author = models.CharField(max_length=50)
    request_date = models.DateTimeField()
    user = models.ForeignKey(userDetails,on_delete=models.CASCADE)
    accepted_date = models.DateTimeField(auto_now_add=True)
    fine = models.IntegerField(default=0)
    return_date = models.DateTimeField()

    def __str__(self):
        return f"request by {self.user.user.user.username} for {self.book_name}"

class Accepted_button_model(models.Model):
    bookname = models.CharField(max_length=50)
    book_image = models.ImageField(upload_to='images/')
    Author = models.CharField(max_length=50)
    request_date = models.DateTimeField()
    userdetails = models.ForeignKey(userDetails, on_delete=models.CASCADE)
    accepted_date = models.DateTimeField(auto_now_add=True)
    fine = models.IntegerField(default=0)
    return_date = models.DateTimeField()
    #
    # def __str__(self):
    #     return f"request by {self.user.user.user.username} for {self.book_name}"

class new_model(models.Model):
    bookname = models.CharField(max_length=50)
    book_image = models.ImageField(upload_to='images/')
    Author = models.CharField(max_length=50)
    request_date = models.DateTimeField()
    userdetails = models.ForeignKey(userDetails, on_delete=models.CASCADE)
    accepted_date = models.DateTimeField(auto_now_add=True)
    fine = models.IntegerField(default=0)
    return_date = models.DateTimeField()

    def __str__(self):
        return f"Accepted request by {self.userdetails.user.username} for {self.bookname}"