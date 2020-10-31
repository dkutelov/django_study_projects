from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template import loader

from polls.forms import QuestionAnswerForm
from polls.models import Question, Choice, ScaleChoice
from django.urls import reverse


def index(req):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    #
    # return HttpResponse(template.render(context, req))
    return render(req, 'polls/index.html', context)


def detail(req, question_id):
    #return HttpResponse("You are looking at question %s." % question_id)
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404('Question does not exists')

    question = get_object_or_404(Question, pk=question_id)
    return render(req, 'polls/detail.html', {'question': question})


def results(req, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(req, question_id):
    question = get_object_or_404(Question, pk=question_id)

    try:
        selected_choice = question.choice_set.get(pk=req.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(req, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice"
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def answer_question(req, question_id):
    question = get_object_or_404(Question, pk=question_id)

    form = QuestionAnswerForm()

    context = {
        'form': form,
        'question': question
    }

    if req.method == 'GET':
        return render(req, 'polls/answer.html', context)

    elif req.method == 'POST':
        form = QuestionAnswerForm(req.POST)
        if form.is_valid():
            # As shown by Doncho
            # answer = ScaleChoice(choice_score=form.cleaned_data['choice_score'])
            # answer.question = question
            # answer.save()
            # question.scalechoice_set.add(answer)
            # question.save()
            # answer = ScaleChoice(choice_score=form.cleaned_data['choice_score'])

            # shorter - also returns the result
            # choice_score = form.cleaned_data['choice_score']
            # question.scalechoice_set.create(choice_score=choice_score)

            # via form
            answer = form.save(commit=False)
            answer.question = question
            answer.save()

            return render(req, 'polls/answer.html', context)