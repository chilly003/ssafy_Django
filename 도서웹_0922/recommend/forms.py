from django import forms
from . models import Report

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = '__all__'
        widgets = {
            'name' : forms.TextInput(
                attrs= {
                    'class': 'form-control',
                    'placeholder': '제목을 입력해주세요.',
                }
            ),
            'author': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '저자를 입력해주세요.',
                }
            ),
            'report': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': '독후감을 작성해 주세요.',
                }
            ),
        }
        labels = {
            'name':'책이름',
            'author':'저자',
            'report': '독후감',
            'is_completed':'작성을 완료하셨나요?',
            'image':'사진 제출',
            'star':'당신의 별점은?'
        }
        error_messages = {
            'name': {
                'invalid': '책 이름을 입력해 주세요!',
            },
            'author':{
                'invalid': '저자를 입력해 주세요!',
            },
            'report':{
                'invalid': '독후감을 입력해 주세요!',
            },
        }