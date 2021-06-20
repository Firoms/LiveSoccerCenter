from django import forms
from django.db import models
from django.forms import fields
from .models import User

class SignupForm(forms.Form):
    ID = forms.CharField(label="아이디", max_length=15)
    PW = forms.CharField(label="비밀번호", widget=forms.PasswordInput)
    PW_C = forms.CharField(label="비밀번호 확인", widget=forms.PasswordInput)
    first_name = forms.CharField(label="닉네임", max_length=10)

class LoginForm(forms.Form):
    ID = forms.CharField(label="아이디", max_length=15)
    PW = forms.CharField(label="비밀번호", widget=forms.PasswordInput)