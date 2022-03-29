from .models import Post
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Submit, Fieldset
from django import forms

class BrowseForm(forms.Form):
    choice = forms.ChoiceField(widget=forms.RadioSelect, choices=[])
    def __init__(self, posts, *args, **kwargs):
            super().__init__(*args, **kwargs)
            choices = []

            for post in posts:
                choices.append((post.slug, post.title))

            self.fields['choice'].choices = choices 
            self.helper = FormHelper(self)
            self.helper.form_method = 'post'
            self.helper.layout = Layout(
                Fieldset(
                    'Choose a Post and Select and Action',
                    'choice'
                ),

                ButtonHolder(
                    Submit('viewPost', 'View Post', css_class='btn btn-lg'),
                    Submit('addPost', 'Add Post', css_class='btn btn-lg'), 
                    Submit('editPost', 'Edit Post', css_class='btn btn-lg'), 
                    Submit('deletePost', 'Delete Post', css_class='btn btn-lg')
                )
            )


class AddEditPostForm(forms.Form):
    postText = forms.CharField(widget=forms.Textarea(attrs={"rows":30, "cols":100}),label='Body')
    postTitle = forms.CharField(max_length=250, label='Subject')
    
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.helper = FormHelper(self)
            self.helper.form_method = 'post'
            self.helper.layout = Layout(
                Fieldset(
                    'Enter Your Post Here',
                    'postTitle',
                    'postText',
                ),
                ButtonHolder(
                    Submit('submit', 'Submit', css_class='btn btn-lg')
                )
            )
