from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# create your views here
monthly_challenges = {
    "january": "Peak",
    "february": "Mindset",
    "march": "Deep work",
    "april": "10 minutes 38 seconds",
    "may": "how to win friends and influence people",
    "june": "Atomic habits",
    "july": "Grit",
    "august": "Think like a manager",
    "september": "Seven habits of highly effective people",
    "october": "mindshift",
    "november": "Learning how to learn",
    "december": "Anything you want"
}

# creat your views here.


def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        captitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{captitalized_month}</a></li>"

    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")

    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


""" 
def monthly_challenge(request, month):
    challenge_text = None
    if month == "january":
        challenge_text = "Eat no meat for the entire month!"
    elif month == "february":
        challenge_text = "Walk for at least 20 minutes every day!"
    elif month == "march":
        challenge_text = "learn Django everyday for 20 mins!"
    else:
        return HttpResponseNotFound("This month is not supported")
    return HttpResponse(challenge_text)

    """


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>This month is not supported!</h1>")
