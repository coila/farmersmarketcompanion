from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from polls.models import Poll, Choice


# Create your views here.


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_poll_list'

    def get_queryset(self):
        """ return the last 5 published polls """
        return Poll.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Poll
    template_name = 'polls/details.html'

class ResultsView(generic.DetailView):
    model = Poll
    template_name = 'polls/results.html'

# def index(request):
#     latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
#     context = { 'latest_poll_list': latest_poll_list }
#     return render(request, 'polls/index.html', context)
#     # return HttpResponse("Hello, world. You're at the poll index.")

def details (request, poll_id):
    try:
        poll = Poll.objects.get(pk=poll_id)
    except Poll.DoesNotExist:
        raise Http404
    return render(request, 'polls/details.html', {'poll': poll})
#     # return HttpResponse("You're looking at poll %s." % poll_id)

# def results(request, poll_id):
#     p = get_object_or_404(Poll, pk=poll_id)
#     return render(request, 'polls/results.html', {'poll':p })
#     # return HttpResponse("You're looking at the results of poll %s." % poll_id)

def vote(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # redisplay the poll voting form
        return render(request, 'polls/details.html', {'poll': p, 'error_message': "You didn't select a choice",})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # always return an HttpResponseRedirect after successfully dealing with POST data. This prevents daa from being posted twice if a user hits the back button
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
    # return HttpResponse("You're voting on poll %s." % poll_id)
