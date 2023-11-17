from django.db import models


# Create your models here.

class Question_LLM(models.Model):
    question_text = models.CharField(max_length=400)
    q_LAI = models.CharField(max_length=50)
    q_date = models.DateTimeField("date occured")
    def __str__(self):
        return self.question_text

class Answer_LLM(models.Model):
    qustion = models.ForeignKey(Question_LLM, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=400)

    def __str__(self):
        return self.answer_text

class Text2json(models.Model):
    title = models.CharField(max_length=200)
    i_LAIa= models.CharField(max_length=30)
    i_LAIb= models.TextField()
    msg_llm = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) # instance will save the time it was saved first time