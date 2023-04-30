from django import forms
from .models import Book, Author, Publisher
# , Message, Comment

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'author', 'publisher', 'publication_date', 'post_photo')

        widgets = {
            'publication_date': forms.DateInput(attrs={'type': 'date'})
        }

    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        self.fields['author'].queryset = Author.objects.all()
        self.fields['publisher'].queryset = Publisher.objects.all()



# class MessageForm(forms.ModelForm):
#     class Meta:
#         model = Message
#         fields = ('title', 'content')
#
#
#
# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = ('author', 'content')