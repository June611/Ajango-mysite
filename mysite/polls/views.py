from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
from .models import Question, Choice

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = { "latest_question_list": latest_question_list}
    return render( request, "polls/index.html",context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question":question} )

def results(request, question_id):
    # response = "You're lokking at the results of question %s."
    # return render(request, "polls/results.html",{"content_to_print" : response% question_id}) # % question_id

    #return HttpResponse(response % question_id)

    question = get_object_or_404(Question, pk=question_id)
    try:
        select_choice = question.choice_set.get(pk =request.POST["choice"] )
    except(KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request,
                      "polls/detail.html",
                      {
                          "question":question,
                          "error_message": "You didn't select a choice"
                      },
                      )
    else:
        select_choice.votes +=1;
        select_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question_id,)))

    
def vote(request, question_id):
    response = "You're voting on question %s."
    return render(request, "polls/vote.html", {"content_to_print": response % question_id})