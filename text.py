import pygame as pg


class Text:
    def __init__(self, text, pos, size=24, font="Roboto"):
        self._text = text
        self._pos = pos
        self._font = pg.font.SysFont("Roboto", 24)
        self._text_to_render = self._font.render(text, True, "black")
        self._rect = self._text_to_render.get_rect()
        self._rect.center = self._pos

    def render_to_screen(self, screen):
        screen.blit(self._text_to_render, self._rect)

    def change_text(self, new_text):
        self._text = new_text
        self._text_to_render = self._font.render(new_text, True, "black")
        self._rect = self._text_to_render.get_rect()
        self._rect.center = self._pos
