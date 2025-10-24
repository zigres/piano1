from pygame import *
from settings import WINDOW_WIDTH, WINDOW_HEIGHT, WHITE, GREY, BLACK
from keys import create_key_rects, draw_keys
from sounds import sounds

font.init()
clock = time.Clock()
screen = display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

pressed = set()
key_rects = create_key_rects(7)
keys_list = list(sounds.keys())

settings_rect = Rect(50, 30, 110, 40)
text_font = font.SysFont(None, 32)
running = True
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False
        if e.type == MOUSEBUTTONDOWN:
            for i, r in enumerate(key_rects):
                if r.collidepoint(e.pos):
                    sounds[keys_list[i]].play()
                    pressed.add(i)
        if e.type == MOUSEBUTTONUP:
            for i in list(pressed):
                if key_rects[i].collidepoint(e.pos):
                    pressed.discard(i)
    screen.fill(WHITE)
    draw.rect(screen, GREY, settings_rect, border_radius=10)
    text = text_font.render("Settings", True, BLACK)
    screen.blit(text, (settings_rect.x +10, settings_rect.y +8))
    draw_keys(screen, key_rects, pressed)
    display.update()
    clock.tick(60)