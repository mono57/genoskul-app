from blog.models import Post
from django import forms



class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'image', 'content', )
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            # 'content': forms.CharField(widget=CKEditorWidget(attrs={'class': 'form-control'})),
        }
    
    def clean_title(self):
        title = self.cleaned_data.get('title')
        qs = Post.objects.filter(title=title)
        if qs.exists():
            raise forms.ValidationError('un article existe avec ce titre')
        return title