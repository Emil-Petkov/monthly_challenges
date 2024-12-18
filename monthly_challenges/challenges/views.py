from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


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


def index(request):
    list_items = ''
    months = list(monthly_chalenges.keys())
    
    for month in months:
        capitalize_month = month.capitalize()
        month_path = reverse('month_challenge', args=[month])
        list_items += f'<li><a href="{month_path}">{capitalize_month}</a></li>'

    response_data = f'<ul>{list_items}</ul>'

    return HttpResponse(response_data)


def monthly_challenge_by_number(request, month):
    months = list(monthly_chalenges.keys())

    if month > 12:
        return HttpResponseNotFound("Month number is out of range.")

    redirect_month = months[month - 1]
    redirect_path = reverse('month_challenge', args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_chalenges[month]
        response_data = f'<h1>{challenge_text}</h1>'
        return HttpResponse(response_data)

    except:
        return HttpResponseNotFound("<h1>Month not found.</h1>")
