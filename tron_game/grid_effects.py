import pygame
import math

def draw_glowing_grid(surface, base_color, spacing, time, thickness=1, glow_layers=3):
    width, height = surface.get_size()

    # Crea una superficie con canal alfa para el resplandor
    glow_surface = pygame.Surface((width, height), pygame.SRCALPHA)

    # Crea capas de resplandor
    for layer in range(glow_layers, 0, -1):
        alpha = int(40 * (layer / glow_layers))  # Menor capa = más transparente
        scale = 1 + 0.5 * (layer / glow_layers)  # Capas externas más gruesas
        color = (*base_color, alpha)

        # Oscilación de brillo
        pulse = (math.sin(time * 2 + layer) + 1) / 2
        color = tuple(int(c * (0.6 + 0.4 * pulse)) for c in base_color) + (alpha,)

        for x in range(0, width, spacing):
            pygame.draw.line(glow_surface, color, (x, 0), (x, height), int(thickness * scale))
        for y in range(0, height, spacing):
            pygame.draw.line(glow_surface, color, (0, y), (width, y), int(thickness * scale))

    # Dibuja la cuadrícula base encima
    for x in range(0, width, spacing):
        pygame.draw.line(glow_surface, base_color + (255,), (x, 0), (x, height), thickness)
    for y in range(0, height, spacing):
        pygame.draw.line(glow_surface, base_color + (255,), (0, y), (width, y), thickness)

    # Superpone el resplandor sobre la superficie principal
    surface.blit(glow_surface, (0, 0))
