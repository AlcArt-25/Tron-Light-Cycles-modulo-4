from enum import Enum

class State(Enum):
    MENU = "MENU"
    COUNTDOWN = "COUNTDOWN"
    GAME = "GAME"
    PAUSE = "PAUSE"
    GAME_OVER = "GAME_OVER"
    OPTIONS = "OPTIONS"
    MODE_SELECT = "MODE SELECT"
