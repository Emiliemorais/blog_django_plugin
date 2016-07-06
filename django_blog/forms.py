from django import forms
from django.utils.translation import ugettext, ugettext_lazy as _
from models import Post


class PostForm(forms.ModelForm):

    
    """PostForm Class. TThis class contains the treatments
     of the existents forms on create post.
    """

    class Meta:

        """Meta Class. This class defines the informations
        that will be used based on existent set
        from Post Model.
        """

        model = Post
        fields = '__all__'
