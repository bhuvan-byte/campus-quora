from django.shortcuts import render
from posts.models import Question,Answer
from django.views import generic
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.

def index(request):
    question_list=Question.objects.all()
    context={
        'question_list':question_list
    }
    return render(request,'index.html',context=context)

class QuestionView(generic.ListView):
    model=Question
    template_name='posts.html'

class QuestionDetailView(generic.DetailView):
    model= Question
    template_name='question_detail.html'

def add_question(request):
    if(request.method=='POST'):
        form=request.POST
        print(type(form['content']))
        newQuestion=Question(content=form['content'])
        newQuestion.save()
        return HttpResponseRedirect(reverse('list'))
    else:
        return render(request,'add_question.html',context=None)
