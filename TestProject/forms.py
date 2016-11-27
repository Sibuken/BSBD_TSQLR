from django.forms.extras import SelectDateWidget
from django.utils.datetime_safe import datetime

from .models import *
from django import forms
#from django.forms.widgets import DateTimeBaseInput
from django.forms import ModelForm, SplitDateTimeWidget
from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget

class TestForm(forms.Form):
	Name = forms.CharField\
        (
            label=" Название теста",
            max_length=30,
            required=True,
			initial = "\"Тест\""
        )
	DateActivate = forms.DateTimeField\
		(
			label="Дата активации",
			input_formats=['%d-%m-%Y %H:%M'],
			required=True,
			help_text = 'DD.MM.YYYY HH:MM',
		)
	Time = forms.IntegerField\
		(
			label="Время на прохождение",
			min_value=0,
			initial=0,
			help_text="(мин)"
		)
	Variants = forms.IntegerField\
    	(
    		label = "Необходимое количество вариантов",
			min_value=0,
			initial=0
    	)
	ConnectDataBase = forms.ModelChoiceField\
		(
			label="BD",
			queryset=ConnectDataBase.objects.all()
		)


class TestPersonForm(forms.Form):
	Test = forms.ModelChoiceField\
		(
			label = "Выбор теста",
			queryset = Test.objects.all()
		)
	Person = forms.ModelMultipleChoiceField\
		(
			label = "Список студентов",
			queryset = MyUser.objects.all(),
			required=False
		)
	Group = forms.ModelMultipleChoiceField\
		(
			label = "Список групп",
			queryset = GP.objects.all(),
			required=False
		)

class AnswerForm(forms.Form):
	pass