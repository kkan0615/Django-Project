from django import forms
from .models import Program, Subject, Chapter
import re

# https://micropyramid.com/blog/django-forms-basics/ -Clean
class ProgramCreateForm(forms.ModelForm):
    class Meta:
        model = Program
        fields = ('title', 'introduction', 'url_key', 'cover', 'codes')

    def clean_url_key(self):
        url_key = self.cleaned_data['url_key']
        regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

        if regex.search(url_key) != None:
            raise forms.ValidationError('url_key should not have speical symbols')

        return url_key

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ('title', 'content')

class ChapterForm(forms.ModelForm):
    class Meta:
        model = Chapter
        fields = ('title', 'number')