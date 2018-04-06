# -*- coding: UTF-8 -*-
from django import forms
from web.models import Topic, Reply

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['subject', 'content', 'poster']

    def __init__(self, *args, **kwargs):
        super(TopicForm, self).__init__(*args, **kwargs)
        self.fields['subject'].label = "討論主題"
        self.fields['content'].label = "討論內容"
        self.fields['poster'].label = "發表人"
        
        
class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['content', 'poster']

    def __init__(self, *args, **kwargs):
        super(ReplyForm, self).__init__(*args, **kwargs)
        self.fields['content'].label = "回覆內容"
        self.fields['poster'].label = "發表人"
        
        
# 使用者登入表單
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = "帳號"
        self.fields['password'].label = "密碼"