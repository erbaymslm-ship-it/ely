# -*- coding: utf-8 -*-
from kivy.uix.screen import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle
from kivy.animation import Animation
from kivy.clock import Clock
from ui.theme import BG_COLOR, TEXT_COLOR


class SplashScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = FloatLayout()
        with layout.canvas.before:
            Color(*BG_COLOR)
            self.rect = Rectangle(size=layout.size, pos=layout.pos)
        layout.bind(size=self._update_rect, pos=self._update_rect)
        self.title_label = Label(text='ELIXIR\nTECHNOLOGY', font_size='42sp', bold=True, color=TEXT_COLOR, halign='center', valign='middle', size_hint=(1, 0.4), pos_hint={'center_x': 0.5, 'center_y': 0.55}, opacity=0)
        self.sub_label = Label(text='GEO ANALYZER', font_size='18sp', color=(1, 0.84, 0, 0.7), halign='center', size_hint=(1, 0.1), pos_hint={'center_x': 0.5, 'center_y': 0.35}, opacity=0)
        self.ver_label = Label(text='v1.0.0', font_size='12sp', color=(0.5, 0.5, 0.5, 1), size_hint=(1, 0.05), pos_hint={'center_x': 0.5, 'center_y': 0.1}, opacity=0)
        layout.add_widget(self.title_label)
        layout.add_widget(self.sub_label)
        layout.add_widget(self.ver_label)
        self.add_widget(layout)

    def _update_rect(self, instance, value):
        self.rect.size = instance.size
        self.rect.pos = instance.pos

    def on_enter(self):
        Animation(opacity=1, duration=1.2).start(self.title_label)
        Clock.schedule_once(lambda dt: Animation(opacity=1, duration=0.8).start(self.sub_label), 0.8)
        Clock.schedule_once(lambda dt: Animation(opacity=1, duration=0.6).start(self.ver_label), 1.4)
        Clock.schedule_once(self._go_to_main, 3.5)

    def _go_to_main(self, dt):
        Animation(opacity=0, duration=0.5).start(self.title_label)
        Animation(opacity=0, duration=0.5).start(self.sub_label)
        Animation(opacity=0, duration=0.5).start(self.ver_label)
