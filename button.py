from text import Text
from colors import *
import pygame as pg


class Button:
    def __init__(self, text, pos, size) -> None:
        self._btn_text = Text(text, pos)
        self._btn_rect = pg.Rect(
            pos[0] - size[0] // 2, pos[1] - size[1] // 2, size[0], size[1]
        )
        self._btn_color = GREY

    def render_to_screen(self, screen) -> None:
        pg.draw.rect(screen, self._btn_color, self._btn_rect)
        self._btn_text.render_to_screen(screen)

    def change_color(self, color):
        self._btn_color = color

    def get_rect(self):
        return self._btn_rect

    def get_text(self) -> str:
        return self._btn_text._text

    def on_click(self, mouse_pos) -> bool:
        if self._btn_rect.collidepoint(mouse_pos):
            return True
        else:
            return False

    def on_hover(self, mouse_pos):
        if self._btn_rect.collidepoint(mouse_pos):
            self.change_color(ORANGE)
        else:
            self.change_color(GREY)

