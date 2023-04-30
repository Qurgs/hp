from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import *
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from .forms import BookForm


def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

# def book_detail(request, pk):
#     book = Book.objects.get(pk=pk)
#     return render(request, 'book_detail.html', {'book': book})

def book_detail(request, pk):
    # Получить объект книги по переданному идентификатору (pk)
    book = get_object_or_404(Book, pk=pk)
    # Создать форму для обновления информации о книге
    form = BookForm(request.POST or None, instance=book)

    # Обработка запросов POST для обновления информации о книге в базе данных
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('book_detail', pk=pk)

    # Отобразить шаблон для отображения информации о книге и формы для ее редактирования
    context = {'book': book, 'form': form}
    return render(request, 'book_detail.html', context)


class BookUpdateView(UpdateView):
    model = Book
    fields = ['title', 'author', 'publisher', 'publication_date']
    template_name = 'book_update.html'
    success_url = reverse_lazy('book_list')

def book_create_view(request):
    form = BookForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('book_list')
    return render(request, 'book_form.html', {'form': form})

def authors_list(request):
    authors = Author.objects.all()
    return render(request, 'authors_list.html', {'authors': authors})


def publisher_list(request):
    publishers = Publisher.objects.all()
    return render(request, 'publisher_list.html', {'publishers': publishers})

