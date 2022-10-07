from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):


    title = forms.CharField(
        max_length=20, 
        required=True, 
        widget=forms.TextInput(
            attrs={'PlaceHolder':'제목을 입력하세요'}
            ),
        )
    audience = forms.IntegerField(
        required=True, 
        widget=forms.TextInput(
            attrs={'PlaceHolder':'관객수를 입력하세요'}
        ),
    )
    release_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    genre = forms.ChoiceField(
        choices=[('코미디', '코미디'), ('공포', '공포'), ('로멘스', '로멘스')],
        required=True)
    score = forms.FloatField(
        widget=forms.NumberInput(attrs={
            'step': 0.5,
            'min': 0,
            'max': 5,
            'PlaceHolder':'점수를 입력하세요',
        })
        )
    poster_url = forms.Textarea(
        )
    
    
    description = forms.Textarea(
        )

    class Meta:
        model = Movie
        exclude = ('author',)