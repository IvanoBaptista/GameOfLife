import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .utils import create_initial_grid, next_gen

def home_page(request) -> HttpResponse:
    return render(request, 'game/home.html')

def game_of_life_view(request):
    rows = 50
    cols = 50
    initial_grid = create_initial_grid(rows, cols)  # Create an initial grid
    context = {
        'initial_grid': initial_grid,
        'rows': rows,
        'cols': cols,
    }
    return render(request, 'game/game_of_life.html', context)

def next_generation_view(request):
    if request.method == 'POST':
        grid = json.loads(request.body)
        next_grid = next_gen(grid)  # Calculate next state of the grid
        return JsonResponse({'next_grid': next_grid})

