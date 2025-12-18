from django import forms
from .models import Comment
from .models import Post
class PostForm(forms.ModelForm):
    """
    Form for creating/editing blog posts. The author is set in the view.
    """
    class Meta:
        model = Post
        fields = ("title", "featured_image", "content", "excerpt")

class CommentForm(forms.ModelForm):
    """
    Form class for users to comment on a post 
    """
    class Meta:
        """
        Specify the django model and order of the fields
        """
        model = Comment
        fields = ("body",)
