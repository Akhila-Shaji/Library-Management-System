from django.urls import path
from .views import *

urlpatterns=[
    path('libraryreg/',lib_Studentreg.as_view(),name='libreg'),
    path('librarylogin/',lib_Login.as_view(),name='liblogin'),
    path('profilepage/',profileview.as_view(),name='profile'),
    path('booksadd/',books_add.as_view(),name='books'),
    path('bookdisplaypage/',books_display_fun.as_view(),name='bookdisplay'),
    path('singleview/<pk>',books_singleview.as_view(),name='view'),
    path('libdispage/',books_display_library.as_view(),name='bookdisplaylib'),
    path('updateprofile/<pk>',edit_profile.as_view(),name='update'),
    path('request/<pk>',request_View.as_view(),name='forbook'),
    path('displayrequest/',display_Request.as_view(),name='req'),
    path('libreqview/',library_Request_view.as_view(),name='libreq'),
    path('acceptpage/<pk>',AcceptButtonView.as_view(),name='accept'),
    path('acceptlistpage/',Accepted_list_view.as_view(),name='listpage'),
    path('studentacceptbook/',student_Accepted_Book_view.as_view(),name='stu_book'),
    path('index/',Library_Index),
    path('editbook/<pk>',library_Book_edit.as_view(),name='editbook'),
    path('Deletebook/<pk>',Delete_books.as_view(),name='del'),
    path('returnbook/<pk>',Return_books.as_view(),name='return'),
    path('Logout_stu/',logout_view.as_view(),name='logout'),



]