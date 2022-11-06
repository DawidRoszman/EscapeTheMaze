import pygame as pg


class Text:
    def __init__(self, text, pos, size=24, font="Roboto", center=True):
        self._text = text
        self._center = center
        self._pos = pos
        self._font = pg.font.SysFont(font, size)
        self._text_to_render = self._font.render(text, True, "black")
        self._rect = self._text_to_render.get_rect()
        if self._center:
            self._rect.center = self._pos
        else:
            self._rect.topleft = self._pos

    def render_to_screen(self, screen):
        screen.blit(self._text_to_render, self._rect)

    def change_text(self, new_text):
        self._text = new_text
        self._text_to_render = self._font.render(new_text, True, "black")
        self._rect = self._text_to_render.get_rect()
        if self._center:
            self._rect.center = self._pos
        else:
            self._rect.topleft = self._pos
