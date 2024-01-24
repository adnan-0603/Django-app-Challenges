from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# create your views here
monthly_challenges = {
    "april": "I want to read 4 books",
    "may": "I want to read 5 books",
    "june": "I want to read 6 books",
    "july": "I want to read 7 books",
    "august": "I want to read 8 books",
    "september": "I want to read 9 books",
    "october": "I want to read 10 books",
    "november": "I want to read 11 books",
    "december": "I want to read 12 books"
}


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


def weekly_challenge(request, day):
    try:
        challenge_text = weekly_challenge[day]
        response_data = f"<h1>{challenge_text}<h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>This week is not supported!<h1>")
