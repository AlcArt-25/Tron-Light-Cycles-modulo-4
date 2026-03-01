import pygame
from .settings import *

def get_first_font(size):
    return pygame.font.Font(str(FONT_TR2N), size)

def get_title_font(size):
    return pygame.font.Font(str(FONT_PRESS_START), size)

def get_menu_font(size):
    return pygame.font.Font(str(FONT_PRESS_START), size)

def get_hud_font(size):
    return pygame.font.Font(str(FONT_PRESS_START), size)

def get_debug_font(size):
    return pygame.font.Font(str(FONT_PRESS_START), size)

def get_game_over_font(size):
    return pygame.font.Font(str(FONT_PRESS_START), size)
