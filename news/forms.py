from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    # content = forms.CharField(label = "", widget = forms.Textarea(
    #     attrs = {

    #     }
    # ))
    class Meta:
        model = Comment
        fields = ['name','email','content']

    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Name'}),label='',max_length=50,required=True) 
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control', 'id':'email', 'placeholder':'Email'}),label='',required=True)
    content = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','placeholder':'write your comment', 'rows':8}),label='',required=True)