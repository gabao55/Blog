from django.forms import ModelForm
from .models import Comments

class FormComment(ModelForm):
    def clean(self):
        data = self.cleaned_data
        name = data.get('comment_name')
        email = data.get('comment_email')
        comment = data.get('comment')

    class Meta:
        model = Comments
        fields = ('comment_name', 'comment_email', 'comment')