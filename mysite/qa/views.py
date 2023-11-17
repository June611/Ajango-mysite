import sys
sys.path.append("D:/15694/my_bin/project_argBrain_LLM/llm_qa/notebooks")
from m import  *    #load llamar2 code
from .models import Question_LLM, Answer_LLM
from django.shortcuts import render
from django.utils import timezone

from django.db import connection
connection.queries

from .models import Question_LLM, Text2json
from django.views import generic
# Create your views here.
from django.contrib.auth.models import User,Group

from rest_framework import  viewsets, generics
from .serializers import UserSerializer, GroupSerializer, Text2jsonSerializer


from django.http import StreamingHttpResponse
from django.views.decorators.http import condition
import time
import json
from urllib.parse import unquote

def index(request):
    #didn't write in database
    return render(request, "qa/index.html",)

def results(request):
    # transaction logic processing layer
    answer = ""
    if request.method == "POST":
        question_ = request.POST.get("question") #get question from form's action
        LAI = request.POST.get("LAI")           #get LAI from form's action
        answer =  fff(question_)                #call llamar2
        if(answer == ""):
            answer = "Nothing! llamar2 don't give a answer!"
        #write data into two tables
        a = Question_LLM.objects.create(question_text=question_,q_LAI = LAI, q_date=timezone.now())
        a.answer_llm_set.create(answer_text = answer)
        #set Q.id is the primary key of answer

    return render(request, "qa/results.html", {"answer": answer, "LAI":LAI,"question":question_})

class ShowallView(generic.ListView):
    #pass the parameter
    template_name = "qa/showall.html"
    context_object_name = "question_list"  #just a note, it has no influence to func:get_queryset

    def get_queryset(self):
        """ return all the question that had been input """
        return Question_LLM.objects.all()

class UserViewSet(viewsets.ModelViewSet):
    """
    all users to check and edit API'path
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """
    all users to check and edit API'path
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class Text2jsonList(generics.ListCreateAPIView):
    queryset = Text2json.objects.all()
    serializer_class = Text2jsonSerializer

class Text2jsonDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Text2json.objects.all()
    serializer_class = Text2jsonSerializer


def event_stream(request):
    # 设置响应头，允许 EventSource 连接
    q_param = request.GET.get('q', '')
    decoded_q = unquote(q_param)

    # print("Info we decode is "  + decoded_q)
    # answer = fff(decoded_q)  # call llamar2
    # if (answer == ""):
    #     answer = "Nothing! llamar2 don't give a answer!"
    # response = StreamingHttpResponse(streaming_content=event_stream_generator(answer))
    response = StreamingHttpResponse(streaming_content=event_stream_generator(decoded_q))
    response['Content-Type'] = 'text/event-stream'
    response['Cache-Control'] = 'no-cache'
    return response

def event_stream_generator(decoded_q):
    # 一个简单的事件生成器，每秒发送一个带有时间戳的消息
    msg= decoded_q
    data = json.dumps({'event': 'lhy', 'data': f'{msg}'})
    yield f"data: {data}\n\n"
    # yield {'event': 'lhy', 'data': f'{msg}'}