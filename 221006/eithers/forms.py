from socket import fromshare
from django import forms
from .models import Question, Comment

class QuestionForm(forms.ModelForm):
    
    issue_a = forms.CharField(label='RED TEAM')
    issue_b = forms.CharField(label='BLUE TEAM')

    class Meta:
        model = Question
        fields = '__all__'


class CommentForm(forms.ModelForm):

    PICKS = [(False, 'RED TEAM'), (True, 'BLUE TEAM')]

    pick = forms.ChoiceField(choices=PICKS, widget=forms.Select())


    class Meta:
        model = Comment
        fields = ['pick', 'content',]