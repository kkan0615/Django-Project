from django import forms
from .models import Community, Post
import re

# https://micropyramid.com/blog/django-forms-basics/ -Clean
class CommunityCreateForm(forms.ModelForm):
    class Meta:
        model = Community
        fields = ('title', 'introduction', 'url_key')

    def clean_url_key(self):
        url_key = self.cleaned_data['url_key']
        regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

        if regex.search(url_key) != None:
            raise forms.ValidationError('url_key should not have speical symbols')

        return url_key

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content')