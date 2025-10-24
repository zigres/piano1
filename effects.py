from pygame import draw
from settings import BLACK

def draw_key_effect(screen, rect, is_pressed=False):
    color = (170,220,225) if is_pressed else (220,220,220)
    draw.rect(screen, color, rect, border_radius=8)
    draw.rect(screen, BLACK, rect, 2, border_radius=8)