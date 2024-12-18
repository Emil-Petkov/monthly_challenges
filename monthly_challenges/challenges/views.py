from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect


monthly_chalenges = {
    'january': 'Eat no meat for the entire month!',
    'february': 'Walk for at least 20 minutes every day!',
    'march': 'Complete at least 2 tasks in your daily routine!',
    'april': 'Create a habit of exercising 30 minutes a day!',
    'may': 'Practice mindfulness 5 times a day!',
    'june': 'Take 5 minutes to meditate every day!',
    'july': 'Create a daily to-do list and prioritize tasks!',
    'august': 'Start a daily journal and write down your thoughts and feelings!',
    'september': 'Create a daily planner and stick to it!',
    'october': 'Make a resolution for the month and celebrate it!',
    'november': 'Start a new year by setting a goal and achieving it!',
    'december': 'Christmas is so close : ).',
}


def monthly_challenge_by_number(request, month):
    months = list(monthly_chalenges.keys())

    if month > 12:
        return HttpResponseNotFound("Month number is out of range.")

    redirect_month = months[month - 1]

    return HttpResponseRedirect('/challenges/' + redirect_month)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_chalenges[month]
        return HttpResponse(challenge_text)

    except:
        return HttpResponseNotFound("Month not found.")
