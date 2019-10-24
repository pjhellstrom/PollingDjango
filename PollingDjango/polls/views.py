from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
from .models import Question, Choice

# Get questions and render on page


def index(request):
    latest_question_list = Question.objects.order_by('-published_date')[:3]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

# Show question and answer choices


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404('Question does not exist...')
    return render(request, 'polls/detail.html', {'question': question})


# Show results for selected question
def results(request, question_id):
    # look in db, if not found return 404
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

# Submit vote


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
