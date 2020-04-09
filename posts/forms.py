from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from . models import Post, Comment
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox



class PostForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())



class Meta:
	model = Post
	fields = '__all__'


class CommentForm(forms.ModelForm):

	name = forms.CharField(label='', widget=forms.TextInput(attrs={
		'class': 'form-control',
		'placeholder': 'Type your name',
		'id': 'username',

		}))

	comment = forms.CharField(label='', widget=forms.Textarea(attrs={
		'class': 'form-control',
		'placeholder': 'Type your comment ',
		'id': 'usercomment',
		'rows': 5,

		}))

	captcha = ReCaptchaField(label='', widget=ReCaptchaV2Checkbox(attrs={
			'class': 'post-captcha',
            'data-theme': 'light',
        }))

	class Meta:
		model = Comment
		fields = ('name', 'comment', )

