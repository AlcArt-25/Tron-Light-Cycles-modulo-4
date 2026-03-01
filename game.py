import pygame, os, random
from arcade_machine_sdk import GameBase, GameMeta
from tron_game.player import Player
from tron_game.ui import *
from tron_game.settings import *
from tron_game.fonts import *
from tron_game.config import *

from tron_game.state_manager import StateManager
from tron_game.state_definitions import State
from tron_game.states.menu_state import MenuState
from tron_game.states.countdown_state import CountdownState
from tron_game.states.game_state import GameState
from tron_game.states.pause_state import PauseState
from tron_game.states.game_over_state import GameOverState
from tron_game.states.option_state import OptionsState
from tron_game.states.mode_select_state import ModeSelectState


class TronGame(GameBase):
    def __init__(self, metadata: GameMeta):
        super().__init__(metadata)
        self.first_font = get_first_font(100)
        self.title_font = get_title_font(50)
        self.menu_font = get_menu_font(20)
        self.hud_font = get_hud_font(15)
        self.go_font = get_game_over_font(70)
        self.countdown_font = get_title_font(60)
        self.title_anim = ColorCycler(interval=600)
        self.current_music = None
        
        p1, p2 = load_controls()
        self.controls_p1 = p1
        self.controls_p2 = p2

        if not os.path.exists(CONFIG_FILE):
            save_controls(self.controls_p1, self.controls_p2)
        
        self.score_p1 = 0
        self.score_p2 = 0
        self.winner = ""
        
        self.player = None
        self.player2 = None

        self.state_manager = StateManager(self)
        self.state_manager.register(State.MENU, MenuState)
        self.state_manager.register(State.COUNTDOWN, CountdownState)
        self.state_manager.register(State.GAME, GameState)
        self.state_manager.register(State.PAUSE, PauseState)
        self.state_manager.register(State.GAME_OVER, GameOverState)
        self.state_manager.register(State.OPTIONS, OptionsState)
        self.state_manager.register(State.MODE_SELECT, ModeSelectState)
        self.menu_music_paths = [str(p) for p in MENU_MUSIC]  # lista de rutas
        self.game_music_path = str(GAME_MUSIC)
        self.state_manager.change(State.MENU, self)
        self.debug = False # Modo debug desactivado por defecto
        
    def start(self, surface: pygame.Surface):   
        super().start(surface)
        
        self.play_menu_music()    
        pygame.mixer.music.set_volume(0.1)
        self.state_manager.change(State.MENU, self)
        
        if self.player is None or self.player2 is None:
            self.reset_game()
        else:
            self.player.load_sprites()
            self.player2.load_sprites()
    
    def stop(self):
        # Detén la música al salir del juego
        pygame.mixer.music.stop()
        super().stop()
        
    def play_menu_music(self):
        if self.current_music != "menu":
            # Elegir una canción aleatoria de la lista
            chosen = random.choice(self.menu_music_paths)
            pygame.mixer.music.load(chosen)
            pygame.mixer.music.play(-1)
            self.current_music = "menu"

    def play_game_music(self):
        if self.current_music != "game":
            pygame.mixer.music.load(self.game_music_path)
            pygame.mixer.music.play(-1)
            self.current_music = "game"     
        
       
    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_F3:
                self.debug = not self.debug
        self.state_manager.handle_events(events)

    def update(self, dt):
        
        self.state_manager.update(dt)
        self.current_fps = int(1 / dt) if dt > 0 else 0
    
    def render(self):
        surface = self.surface
        surface.fill(BLACK)
        self.state_manager.render(surface)
        
        if self.debug:
            fps_text = self.hud_font.render(f"FPS: {self.current_fps}", True, WHITE)
            surface.blit(fps_text, (10, 10))

    def reset_game(self):
        # Elegir colores aleatorios distintos
        color1 = random.choice(COLORS_VAR)
        remaining_colors = [c for c in COLORS_VAR if c != color1]
        color2 = random.choice(remaining_colors) if remaining_colors else color1

        name1 = COLOR_NAMES.get(color1, "cyan")
        name2 = COLOR_NAMES.get(color2, "naranja")
        
        #Posiciones iniciales
        start_col1 = 10
        start_col2 = (WIDTH // CELL_SIZE) - start_col1
        start_row = (HEIGHT // CELL_SIZE) // 2  # fila central
        
        self.player = Player(start_col1, start_row, color1, self.controls_p1, name1)
        self.player2 = Player(start_col2, start_row, color2, self.controls_p2, name2)
        self.player.load_sprites()
        self.player2.load_sprites()

        # Establecer direcciones iniciales
        self.player.direction = None
        self.player2.direction = None

        # Reiniciar variables de estado
        self.winner = ""
        self.game_start_time = None

    def reset_all(self):
        self.score_p1 = 0
        self.score_p2 = 0
        self.reset_game()

metadata = (
    GameMeta()
    .with_title("Tron Light Cycles")
    .with_description("Juego de motos de luz estilo TRON para dos jugadores")
    .with_release_date("2026-03-05")
    .with_group_number(4)
    .add_author("Victor Alcala")
    .add_author("Ricardo Trevison")
    .add_tag("Arcade")
    .add_tag("Retro")
    .add_tag("Multijugador")
)

if __name__ == "__main__":
    if not pygame.get_init():
        pygame.init()
    game = TronGame(metadata)
    game.run_independently()
