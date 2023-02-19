from django.shortcuts import render

# Create your views here.
def bz(request):
    return render(request, 'База-знаний.html')

def achievements(request):
    return render(request, 'Достижения.html')

def progress_map(request):
    return render(request, 'Карта-прогресса.html')

def progress_cell_card(request):
    return render(request, 'Карточка-ячейки-прогресса.html')

def Second_cell_card(request):
    return render(request, 'Карточка-второй-ячейки.html')

def third_cell_card(request):
    return render(request, 'Карточка-третьей-ячейки.html')

def contacts(request):
    return render(request, 'Контакты.html')

def events(request):
    return render(request, 'Мероприятия.html')

def profile(request):
    return render(request, 'Профиль.html')