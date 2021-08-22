from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Event
import sqlite3
from django import forms

@login_required
def indexView(request):
    return render(request, 'pages/index.html')

@login_required
def eventView(request, userid):
    events = Event.objects.filter(user=userid)
    notes = [{'id': e.id, 'date': e.date, 'event': e.event} for e in events]
    return render(request, 'pages/events.html', {'notes': notes})

@login_required
def addView(request):
    if request.method == 'POST':
        name = request.POST.get('event', '').strip()
        date1 = request.POST.get('date', '')
        note = Event(event = name, date = date1, user = request.user)
        note.save()
        return redirect('/')

@login_required
def deleteView(request):
    e = Event.objects.get(pk=request.POST.get('id'))
    e.delete()
    return redirect('/')


