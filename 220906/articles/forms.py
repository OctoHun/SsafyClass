from django import forms
from .models import Article

# class ArticleForm(forms.Form):
#     NATION_A = 'kr'
#     NATION_B = 'ch'
#     NATION_C = 'jp'
#     # 튜플 형태
#     NATIONS_CHOICES = [
#         (NATION_A, '한국'),
#         (NATION_B, '중국'),
#         (NATION_C, '일본'),
#     ]
#     title = forms.CharField(max_length=10)
#     content = forms.CharField(widget=forms.Textarea())
#     nation = forms.ChoiceField(choices=NATIONS_CHOICES)
#     # nation = forms.ChoiceField(choices=NATIONS_CHOICES, widget=forms.RadioSelect())

class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        widget=forms.TextInput(
            # attributes
            attrs={
                'class': 'my-title form-control',
                'placeholder': 'Enter the title',
                'maxlength': 10,
            }
        ),
    )

    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={
                'class':'my-content form-control',
                'placeholder':'Enter the content',
                'rows':5,
                'cols':50,
            }
        ),
        error_messages={
            'required':'Please enter your content'
        }
    )

    class Meta:
        model = Article # 어떤 모델을 기반으로 할지
        fields = '__all__'  # 모델 필드 중 어떤 것을 출력할지
        # 원래 튜플로 작성 함. ('title', 'content')