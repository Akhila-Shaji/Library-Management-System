from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import generic
from .forms import *
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import get_object_or_404
from django.contrib.auth import logout

# Create your views here.
class lib_Studentreg(generic.CreateView):
    form_class = Student_Registration
    template_name = 'library.html'
    success_url = reverse_lazy('liblogin')
    def form_valid(self, form):
        user = form.save(commit=False)
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        department = form.cleaned_data['department']
        college_name =form.cleaned_data['college_name']
        roll_no = form.cleaned_data['roll_no']
        register_id= form.cleaned_data['register_id']
        phone=form.cleaned_data['phone']
        userDetails.objects.create(user=user,department=department,college_name=college_name,roll_no=roll_no,register_id=register_id,phone=phone)
        return super().form_valid(form)

class lib_Login(generic.View):
    form_class = AuthenticationForm
    template_name = 'librarylogin.html'
    def get(self, request):
        form = AuthenticationForm
        return render(request, 'librarylogin.html', {'form': form})
    def post(self, request):
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                request.session['userid'] =user.id
                return redirect('profile')
            else:
                return HttpResponse('invalid credentials')
        else:
            return HttpResponse('form is invalid')

#
# class profileview(generic.DetailView):
#     model = userDetails  # connection create cheytath kond User model is also available. because user details model make connection with userDetails
#     template_name = 'profileview.html'
#     context_object_name = 'user'
#     def get_object(self):  # built in function
#         user=self.request.user   # this is the method that is used to get the details of current logged in user. request.user is an in-built function
#         return get_object_or_404(userDetails,user=user) # it returns the user details that mathches the user data that are logged in


# alternate method
class profileview(generic.DetailView):
    model = userDetails  # connection create cheytath kond User model is also available. because user details model make connection with userDetails
    template_name = 'profileview.html'
    context_object_name = 'user'
    def get_object(self):  # built in function
        user_id = self.request.session.get('userid')
        return userDetails.objects.get(user_id=user_id)


class books_add(generic.CreateView):
    form_class = book_detail_form
    template_name = 'add_bookdetails.html'
    success_url = reverse_lazy('bookdisplaylib')

class books_display_library(generic.ListView):
    model = Library_Book_Details
    template_name = 'librarybooks.html'
    context_object_name = 'data'


def Library_Index(request):
    return render(request,'library_index.html')

# class index_class(generic.View):
#     def get(self,request):
#         return render(request,'index_page.html')

class books_display_fun(generic.ListView):
    model = Library_Book_Details
    template_name = 'displaybook.html'
    context_object_name = 'data'

class books_singleview(generic.DetailView):
    model = Library_Book_Details
    template_name = 'books_detail_view.html'
    context_object_name = 'book'

class library_Book_edit(generic.UpdateView):
    model = Library_Book_Details
    template_name = 'Update_book.html'
    fields = ['book_name','book_image','Author','description','available_copies']
    success_url = reverse_lazy('bookdisplay')

class Delete_books(generic.DeleteView):
    model = Library_Book_Details
    template_name = 'delete_Books.html'
    success_url = reverse_lazy('bookdisplay')


class edit_profile(generic.UpdateView):
    model = User
    form_class = Editprofile
    template_name = 'profileedit.html'
    success_url = reverse_lazy('profile')

    def get_object(self):       # its a built in function. any dictionary coming to function for eg:pk get cheyyan. functionilek pass cheyyunna data edukan
        user=super().get_object()        # user pkne get cheyunnu. userilek edutha data store cheyunnu. get the person with speciic id passing into the url
        self.userDetails_instance = userDetails.objects.get(user=user) # userdetailsile oro fields aanu instances. corresponding data oro instancilek store ccheyunnu. modelile corresponding variabilek store cheyunnu
        return user   #

 #  the instance value which is used in django forms to specify which particular instance the form is prefilled.
 # what happens is that the form is filled with the data from the particular record

    def get_form(self, form_class=None):    # get_form used to modify the forms that to be returned. its a built in function
        form = super().get_form(form_class)  # we get the form_class of Editprofile
        form.fields['department'].initial = self.userDetails_instance.department # initial value aayi store cheyt veykuka. already ulla datas.
        form.fields['phone'].initial = self.userDetails_instance.phone
        form.fields['register_id'].initial = self.userDetails_instance.register_id
        form.fields['roll_no'].initial = self.userDetails_instance.roll_no
        form.fields['college_name'].initial = self.userDetails_instance.college_name
        return form

    def form_valid(self, form):
        response = super().form_valid(form)  # get_formil return cheyta form form_validilek pass cheyt
        self.userDetails_instance.department = form.cleaned_data['department']
        self.userDetails_instance.phone = form.cleaned_data['phone']
        self.userDetails_instance.register_id =  form.cleaned_data['register_id']
        self.userDetails_instance.roll_no = form.cleaned_data['roll_no']
        self.userDetails_instance.college_name = form.cleaned_data['college_name']
        self.userDetails_instance.save()
        return response


# exist is a built in function to check whether the object is exist. if exist returns true, else return false

# get_object or 404 : it gets the object otherwise it returns 404 error

class request_View(generic.View):
    def get(self,request,pk):
        book = get_object_or_404(Library_Book_Details,id=pk)
        user_details = get_object_or_404(userDetails,user=request.user)

        if BookRequest.objects.filter(user=user_details,book=book).exists():
            return redirect('req')
        else:
            BookRequest.objects.create(user=user_details,book=book)
            # return redirect('req')
            return HttpResponse('your request is successfully added')


class display_Request(generic.ListView):
    model = BookRequest
    template_name = 'displayrequest.html'
    context_object_name = 'books'
    def get_queryset(self):
        user = self.request.user
        return BookRequest.objects.filter(user__user__id=user.id)

# you can override your query in list view using get_queryset(). we can modify the query


class library_Request_view(generic.ListView):
    model = BookRequest
    template_name = 'lib_request_view.html'
    context_object_name = 'book'

import datetime
from datetime import timedelta

from django.utils import timezone
class AcceptButtonView(generic.View):
    def get(self, request, pk):
        bookreq = BookRequest.objects.get(id=pk)  # book request modelile items eduth particular id ulla aale get cheyunnu
        book =get_object_or_404(Library_Book_Details, book_id=bookreq.book.book_id)
        new_model.objects.create(
            bookname = bookreq.book.book_name,
            book_image =bookreq.book.book_image,
            Author = bookreq.book.Author,
            request_date =bookreq.request_date,
            userdetails = bookreq.user,
            return_date =timezone.now()+timedelta(days=10)

        )
        if book.available_copies > 0:
            book.available_copies -= 1
            book.save()
        else:
            return HttpResponse('No available copies left')
        bookreq.delete()
        return HttpResponse('accepted')

# fine calculation must be carry out on the view page
class Accepted_list_view(generic.ListView):
    model = new_model
    template_name = 'accepted_book_list.html'
    context_object_name = 'data'

    def get_queryset(self):
        query_set = super().get_queryset()  # Get the default queryset (equivalent to objects.all())
        current_date = timezone.now()

        for accepted_book in query_set:
            if current_date > accepted_book.return_date:
                overdue = (current_date - accepted_book.return_date).days
                accepted_book.fine = overdue * 10
            else:
                accepted_book.fine = 0
            accepted_book.save()
        return query_set

class student_Accepted_Book_view(generic.ListView):
    model = new_model
    template_name = 'stu_accepted_book.html'
    context_object_name = 'accepted_books'
    def get_queryset(self):
        user = self.request.user
        query_set = new_model.objects.filter(userdetails__user__id=user.id)
        current_date = timezone.now()
        for accepted_book in query_set:
            if current_date > accepted_book.return_date:
                overdue = (current_date - accepted_book.return_date).days
                accepted_book.fine = overdue * 10
            else:
                accepted_book.save()
        return query_set

class Return_books(generic.DeleteView):
    model = new_model
    template_name = 'return_books.html'
    success_url = reverse_lazy('listpage')

class logout_view(generic.View):
    def get(self,request):
        logout(request)
        return redirect('liblogin')













