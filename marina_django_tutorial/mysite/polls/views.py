import json, logging
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404, HttpResponseRedirect, HttpResponseBadRequest
from django.core.urlresolvers import reverse
from django.views import generic
from polls.models import Poll, Choice


# Create your views here.

# class BaseView(generic.ListView):
    # template_name = 'polls/base.html'

# class IndexView(generic.ListView):
#     template_name = 'polls/index.html'
#     context_object_name = 'latest_poll_list'

#     def get_queryset(self):
#         """ return the last 5 published polls """
#         return Poll.objects.order_by('-pub_date')[:5]

#     def show(self, request):
#         template_name = "partial_results.html"
#         return HttpResponse(template_name)

class DetailView(generic.DetailView):
    model = Poll
    template_name = 'polls/details.html'

class ResultsView(generic.DetailView):
    model = Poll
    template_name = 'polls/results.html'

def index(request):
    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    context = { 'latest_poll_list': latest_poll_list }
    return render(request, 'polls/index.html', context)

def search_form(request):
    return render(request, 'polls/search_form.html')



def search(request):
    if request.method == 'GET':
        response_data = {}
        text = request.GET.get('statecode')
        message = text
        response_data['result'] = text
        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        message = "OOPS, somethign went wrong"
    return render(request, 'polls/index.html', message)


def getResults(zipcode):
    # r = urllib2.urlopen('http://search.ams.usda.gov/farmersmarkets/v1/data.svc/zipSearch?zip=' + zipcode)
    result = json.load(zipcode)
    logging.warning(str(result))
    logging.warning('I ma here')
    pattern = re.compile(r'[0-9.]')
    for market in result['results']:
        market['distance'] = ''.join(pattern.findall(market['marketname']))
        market['marketname'] = ''.join([i for i in market['marketname'] if not i.isdigit()]).strip('.')
    response_data = {}
    response_data['result'] = result['results']
    return HttpResponse(
        json.dumps(response_data),
        content_type="application/json"
    )
    # return render(request, 'polls/index.html', message)





def details (request, poll_id):
    try:
        poll = Poll.objects.get(pk=poll_id)
    except Poll.DoesNotExist:
        raise Http404
    return render(request, 'polls/details.html', {'poll': poll})

# def results(request, poll_id):
#     p = get_object_or_404(Poll, pk=poll_id)
#     return render(request, 'polls/results.html', {'poll':p })
#     # return HttpResponse("You're looking at the results of poll %s." % poll_id)

def vote(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/details.html', {'poll': p, 'error_message': "You didn't select a choice",})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))






