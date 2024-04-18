from django.forms import ModelForm,Textarea
from Blog_App.models import Comments, Likes


class CommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = ['comment']