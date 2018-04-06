# -*- coding: UTF-8 -*-
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.shortcuts import render
from models import Topic, Reply
from django.utils import timezone
from forms import TopicForm, ReplyForm, LoginForm
from django.contrib.auth import authenticate, login

def index(request):
    topics = Topic.objects.all().order_by("-reply_date")
    return render_to_response('index.html', {'topics': topics}, context_instance=RequestContext(request))

def add(request):
    if request.method == 'POST':
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = TopicForm()
        return render_to_response('form.html',{'form': form}, context_instance=RequestContext(request))

def show(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    replys = Reply.objects.filter(topic_id=topic_id).order_by("-id")
    return render_to_response('show.html', {'topic': topic, 'replys': replys}, context_instance=RequestContext(request))
  
  
def reply(request, topic_id):
    if request.method == 'POST':
        form = ReplyForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.topic_id = topic_id
            reply.save()
            topic = Topic.objects.get(id=topic_id)
            topic.reply_date = timezone.now()
            topic.save()
            return redirect("/")
    else:
        form = ReplyForm()
        return render_to_response('form.html',{'form': form}, context_instance=RequestContext(request))
      
      
# 使用者登入功能
def user_login(request):
    message = ""
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                # 登入成功，導到大廳
                login(request, user)
                return redirect('/')
            else:
                message = "無效的帳號或密碼!"
    else:
        form = LoginForm()
    return render_to_response('login.html', {'message': message, 'form': form}, context_instance=RequestContext(request))