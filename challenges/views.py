from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


monthly_challenges = {
    "january": "Eat no meat for the entire month",
    "february": "Walk for at least 20 mins per day",
    "march": "Learn Django for at least 20 mins per day",
    "april": "Eat more greens each day",
    "may": "Walk for at least 20 mins per day",
    "june": "Summber vacations in this month",
    "july": "Learn Django for at least 20 mins per day",
    "august": "Eat more greens each day",
    "september": "Learn Django for at least 20 mins per day",
    "october": "Eat more greens each day",
    "november": "Walk for at least 20 mins per day",
    "december": "End of year. No task.",
}

# Create your views here.


def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        capitalised_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalised_month}</li>"

    response_date = f"<ul>{list_items}</ul>"

    return HttpResponse(response_date)


def monthly_challenges_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")

    redirect_month = months[month - 1]
    redirect_path = reverse(
        "month-challenge", args=[redirect_month])  # /challenge/january

    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month_name": month,
        })
    except:
        return HttpResponseNotFound("This month is not supported")
