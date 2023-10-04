import time

from django.shortcuts import render, redirect
from django.views.generic import DetailView,UpdateView,DeleteView,CreateView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin

from .forms import BookForm,AuthorForm
from .models import Author,Book


# Saytning asosiy  homepage
def book_views(request):

    search=request.GET.get("search")
    books = (Book.objects.all().prefetch_related('author')).order_by('title')

    if search:
        books =(books.filter(title__contains=search)
                |books.filter(genre__contains=search)
                |books.filter(author__name__contains=search)
                |books.filter(author__surname__contains=search))
    else:
        search=str()

    return render(request,"kutubxona/book.html",{
      "books": books,"search":search,
    })


# Kitob muallifi yaratish
def author_views(request):

   authors=Author.objects.all()
   return render(request, "kutubxona/author.html", {
       "authors": authors,
   })

# Sayt haqida ma`lumot
def about_views(request):
    return render(request,"kutubxona/about.html")


 # Kitobni o`qish uchun class
class BookDetailView(DetailView):
    model = Book
    template_name ="kutubxona/book_detail.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'


# Kitobni tahrirlash
class BookUpdateView(LoginRequiredMixin,UpdateView):
    model = Book
    template_name = 'kutubxona/book_update.html'
    fields = ['title','author','genre','picture','body','slug']
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    # Qayta yo'naltirish uchun url
    def get_success_url(self):
        return reverse('books')



# Kitobni o`chirish
class BookDeleteView(LoginRequiredMixin,DeleteView,UserPassesTestMixin):
    model = Book
    template_name = 'kutubxona/book_delete.html'
    success_url = reverse_lazy('books')
    slug_field = 'slug'
    slug_url_kwarg = 'slug'



# Kitob yaratish
class BookCreateView(LoginRequiredMixin,CreateView,UserPassesTestMixin):
    model = Book
    template_name = "kutubxona/book_create.html"
    fields = ('title','author','genre','picture','body','slug',)

    # Qayta yo'naltirish uchun url
    def get_success_url(self):
        return reverse('books')

    # user superuser ekanini tekshirish
    def test_func(self):
        return self.request.user.is_superuser

    # user superuser ekanini tekshirish
    # def test_func(self):
    #     return self.request.user.is_superuser



# Muallif uchun view
def author_create_view(request):
    if request.method == 'GET':
        form = AuthorForm()


    else:
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('author_create')


    return render(request, 'kutubxona/krish.html')



# krish qismi 1
def krish_views(request):
    return render(request,'kutubxona/krish.html')

# krish qismi 2
def krish2_views(request):
    return render(request,'kutubxona/krish2.html')




# def book_create_view(request):
#     if request.method == 'GET':
#         form = BookForm()
#
#     else:
#         form = BookForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('book_create')
#
#     return render(request, 'kutubxona/book_create.html', {'form': form})


