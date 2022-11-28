from django import forms
from .models import VisitorsModel, GetInTouchModel
from django.forms import TextInput, Textarea


class FeedbackRegularVisitors(forms.ModelForm):
    """Форма отзывов постоянных клиентов"""
    class Meta:
        model = VisitorsModel  # модель с которой работает форма
        fields = '__all__'  # поля доступные в форме
    image = forms.FileField()


class GetInTouchForm(forms.ModelForm):
    """Форма обращения за помощью к клинике"""
    class Meta:
        model = GetInTouchModel  # модель с которой работает форма
        fields = '__all__'  # поля доступные в форме
        """Виджеты помогают задать форме определенные параметры для редактирования ее с помощью css и не только"""
        widgets = {
            "message": Textarea(attrs={
                'class': 'form-control w-100',
                'id': 'message',
                'cols': '30',
                'rows': '9',
                'onfocus': "this.placeholder = ''",
                'onblur': "this.placeholder = 'Enter Message'",
                'placeholder': "Enter message",
            }),
            "name": TextInput(attrs={
                'class': 'form-control valid',
                'id': 'name',
                'onfocus': "this.placeholder = ''",
                'onblur': "this.placeholder = 'Enter your name'",
                'placeholder': "Enter your name",
            }),
            "email": TextInput(attrs={
                'class': 'form-control valid',
                'id': 'email',
                'onfocus': "this.placeholder = ''",
                'onblur': "this.placeholder = 'Enter email address'",
                'placeholder': "Email",
            }),
            "subject": TextInput(attrs={
                'class': 'form-control',
                'id': 'subject',
                'onfocus': "this.placeholder = ''",
                'onblur': "this.placeholder = 'Enter Subject'",
                'placeholder': "Enter Subject",
            }),
        }
