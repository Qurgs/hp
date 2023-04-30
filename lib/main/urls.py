from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *

urlpatterns = [
    path('', book_list, name='book_list'),
    path('books/<int:pk>/', book_detail, name='book_detail'),
    path('book/<int:pk>/update/', BookUpdateView.as_view(), name='book_update'),
    path('authors/', authors_list, name='authors_list'),
    path('publishers/', publisher_list, name='publisher_list'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)