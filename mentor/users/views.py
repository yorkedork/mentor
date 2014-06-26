import datetime
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils.timezone import utc
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from mentor.questionaire.models import Questionaire, QuestionaireHistory, VIEWED, RESOLVED, UNRESOLVED
from mentor.questionaire.forms import QuestionaireForm
from .perms import decorators

# Create your views here.
@decorators.can_view_mentor_homepage
def mentor_home(request):
    responses = Questionaire.objects.all().order_by("-pk")

    # Using Paginator from Django
    paginator = Paginator(responses, 50) # Show 10 responses per page

    page = request.GET.get('page')
    try:
        responses = paginator.page(page)
    except PageNotAnInteger:
        responses = paginator.page(1)
    except EmptyPage:
        responses = paginator.page(paginator.num_pages)

    return render(request, "mentor/home.html", {
        "responses" : responses,
        "RESOLVED": RESOLVED,
        "UNRESOLVED": UNRESOLVED,
    })

# Detail response for mentor to view
@decorators.can_view_response_detail
def response_detail(request, response_id):
    response = get_object_or_404(Questionaire, pk=response_id)

    history = QuestionaireHistory.objects.filter(
        questionaire=response
    ).select_related(
        "user"
    ).filter(
        action__in=[RESOLVED, UNRESOLVED]
    )

    form = QuestionaireForm(instance=response)

    if not QuestionaireHistory.objects.filter(user=request.user, questionaire=response, action=VIEWED).exists():
        QuestionaireHistory(user=request.user, questionaire=response, action=VIEWED).save()

    return render(request, "mentor/response_detail.html", {
        "response": response,
        "history": history,
        "RESOLVED": RESOLVED,
        "UNRESOLVED": UNRESOLVED,
        "form": form,
    })

@decorators.can_resolve_response
def response_resolve(request, response_id):
    """Toggle the status of the questionaire"""
    response = get_object_or_404(Questionaire, pk=response_id)
    if response.status == RESOLVED:
        response.status = UNRESOLVED
        messages.success(request, "Unresolved")
    elif response.status == UNRESOLVED:
        response.status = RESOLVED
        messages.success(request, "Resolved!")
    response.save()

    QuestionaireHistory(user=request.user, questionaire=response, action=response.status).save()
    return HttpResponseRedirect(reverse('mentor-homepage'))

