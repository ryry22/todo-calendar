from datetime import datetime, timedelta
import calendar as cal
from django.shortcuts import render, get_object_or_404, redirect
from calendar_app.models import Event
from .forms import EventForm
from django.http import JsonResponse

def calendar(request, year=None, month=None):
    today = datetime.today()
    current_year = today.year if year is None else int(year)
    current_month = today.month if month is None else int(month)

    previous_date = datetime(current_year, current_month, 1) - timedelta(days=1)
    previous_year = previous_date.year
    previous_month = previous_date.month
    next_date = datetime(current_year, current_month, 28) + timedelta(days=7)
    next_year = next_date.year
    next_month = next_date.month

    _, num_days = cal.monthrange(current_year, current_month)
    calendar_matrix = cal.monthcalendar(current_year, current_month)

    calendar_rows = []
    for week in calendar_matrix:
        row = []
        for day in week:
            if day == 0:
                row.append(None)
            else:
                date = datetime(current_year, current_month, day)
                day_of_week = date.strftime("%a")
                row.append((day, day_of_week))
        calendar_rows.append(row)

    years = range(current_year - 10, current_year + 11)  # 10年前から10年後までの範囲の年を取得
    months = range(1, 13)  # 1から12までの月を取得

    return render(request, 'calendar.html', {
        'calendar_rows': calendar_rows,
        'current_year': current_year,
        'current_month': current_month,
        'previous_year': previous_year,
        'previous_month': previous_month,
        'next_year': next_year,
        'next_month': next_month,
        'years': years,
        'months': months,
    })

def event(request, year, month, day):
    events = Event.objects.all()
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            # 入力されたデータを保存
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            event = Event(title=title, description=description)
            event.save()
            form = EventForm()
    else:
        form = EventForm()

    return render(request, 'event.html', {
        'year': year,
        'month': month,
        'day': day,
        'form': form,
        'events': events
    })

def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            # 入力されたデータを保存
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            event = Event(title=title, description=description)
            event.save()
            return redirect('event_list')
    else:
        form = EventForm()

    return render(request, 'event.html', {'form': form})

def edit_event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('event_list')
    else:
        form = EventForm(instance=event)
    return render(request, 'event.html', {'form': form})

def delete_event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    if request.method == 'POST':
        event.delete()
        events = Event.objects.all()  # 更新されたイベントリストを取得
        events = [{'id': e.id, 'title': e.title} for e in events]
        return JsonResponse({'message': '削除が成功しました。', 'events': events})
    return render(request, 'event.html', {'event': event})

def event_detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    return render(request, 'event_detail.html', {'event': event})

def calendar_view(request):
    today = datetime.today()
    current_year = today.year
    current_month = today.month
    context = {
        'current_year':current_year,
        'current_month':current_month,
        'today': today,
    }
    return render(request, 'calendar.html', context)

def event_list(request):
    events = Event.objects.all()
    return render(request, 'event.html', {'events': events})