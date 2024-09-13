import pygame

# Configuratie van het scherm
WIDTH, HEIGHT = 800, 600
GRID_SIZE = (50, 50)  # Het aantal rijen en kolommen in het grid
zoom_factor = 10  # Start zoom-factor (celgrootte in pixels)

# Kleurinstellingen
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Pygame initialiseren
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game of Life - Zoom Functie")

# Functie om een leeg grid te tekenen
def draw_grid(screen, zoom_factor):
    # Stel dat dit de lege grid is, gevuld met nullen (levende of dode cellen zouden hier worden gebruikt)
    grid = [[0 for _ in range(GRID_SIZE[0])] for _ in range(GRID_SIZE[1])]
    
    rows, cols = len(grid), len(grid[0])
    
    for row in range(rows):
        for col in range(cols):
            # In dit voorbeeld zijn alle cellen "dood" (zwart), je kunt dit later aanpassen voor levensstatussen
            color = WHITE if grid[row][col] == 1 else BLACK
            rect = pygame.Rect(col * zoom_factor, row * zoom_factor, zoom_factor, zoom_factor)
            pygame.draw.rect(screen, color, rect, 1)  # De cellen tekenen als rechthoeken

# Hoofdprogramma loop
running = True
while running:
    screen.fill(BLACK)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:  # Zoom in met de pijl omhoog
                zoom_factor += 1
            elif event.key == pygame.K_DOWN:  # Zoom uit met de pijl omlaag
                zoom_factor = max(1, zoom_factor - 1)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:  # Muiswiel omhoog (zoom in)
                zoom_factor += 1
            elif event.button == 5:  # Muiswiel omlaag (zoom uit)
                zoom_factor = max(1, zoom_factor - 1)

    # Grid tekenen met de huidige zoomfactor
    draw_grid(screen, zoom_factor)
    
    # Scherm bijwerken
    pygame.display.flip()

pygame.quit()
