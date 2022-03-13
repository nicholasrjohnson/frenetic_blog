from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Submit, Fieldset
from django import forms

class BrowseFrom(forms.Form):
    def __init__(self, *args, **kwargs):
            super()._init__(*args, **kwargs)
            self.helper = FormHelper(self)
            self.helper.form_method = 'post'
            self.helper.layout = Layout(
                Fieldset(

                ),

                ButtonHolder(
                   Submit('viewPost', 'View Post', css_class='') 
                   Submit('viewPost', 'View Post', css_class='') 
                   Submit('viewPost', 'View Post', css_class='') 
                )
            )


class AddEditPostForm(forms.Form):
    def __init__(self, *args, **kwargs):
            super()._init__(*args, **kwargs)
            self.helper = FormHelper(self)
            self.helper.form_method = 'post'
