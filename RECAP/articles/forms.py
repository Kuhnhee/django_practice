from django import forms
from .models import *

# Form class version
# class ArticleForm(forms.Form):
#     # title = forms.CharField(max_length=50)
#     title = forms.CharField(
#         max_length=20,
#         label='제목',
#         help_text='제목은 20자 이내로 써주세요.',
#         widget=forms.TextInput(
#             attrs={
#                 'class': 'form-control my-content',
#                 'placeholder': '제목을 입력해주세요.',
#             }
#         )
#     )
#     content = forms.CharField(
#         label='내용',
#         widget=forms.Textarea(
#             attrs={
#                 'class': 'form-control my-content',
#                 'placeholder': '내용을 입력해주세요',
#                 'rows': 5,
#                 # 'cols': 50, #cols 지정은 따로 안바꿔주는게 좋음. grid를 따르자
#             }
#         )
#     )


# Model Form version
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        # fields = '__all__' #model의 모든 field들을 가지고 오게 됨
        fields = ('title', 'content', )
        #exclude = ('title',)

        '''
        권장되지 않는 위젯 작성법
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': '제목을 입력해 주세요.',
                'class': 'form-control title-class',
                'id': 'title',
            }),
            'content': ...
        }

        label = {
            'title': ...
        }
        '''

    title = forms.CharField(
        max_length=20,
        label='제목',
        help_text='제목은 20자 이내로 써주세요.',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control my-content',
                'placeholder': '제목을 입력해주세요.',
            }
        )
    )
    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control my-content',
                'placeholder': '내용을 입력해주세요',
                'rows': 5,
                # 'cols': 50, #cols 지정은 따로 안바꿔주는게 좋음. grid를 따르자
            }
        )
    )



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        # fields = '__all__'
        fields = ('content',)

    # content = forms.CharField(
    #     max_length=20,
    #     label='댓글',
    #     widget=forms.TextInput(
    #         attrs={
    #             'class': 'form-control my-content',
    #             'placeholder': '댓글 내용을 입력하세요',
    #         }
    #     )
    # )