from django.forms import ModelForm, Textarea
from .models import Post, Comment


class NewPostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['headline', 'text']
        widgets = {
            'text': Textarea(attrs={'cols': 80, 'rows': 20}),
        }


class ReplyForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': Textarea(attrs={'cols': 80, 'rows': 20}),
        }
