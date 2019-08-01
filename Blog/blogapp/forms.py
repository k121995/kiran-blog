from django import forms

class EmailForm(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    to=forms.EmailField()
    comment=forms.CharField(required=False,widget=forms.Textarea)


from blogapp.models import comment
class CommentForm(forms.ModelForm):
    class Meta:
        model=comment
        fields=('name','email','body')
