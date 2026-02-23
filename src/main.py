import kivy
kivy.require('2.0.0')

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from ui.splash import SplashScreen


class ElixirApp(App):
    def build(self):
        sm = ScreenManager(transition=FadeTransition())
        sm.add_widget(SplashScreen(name='splash'))
        return sm


if __name__ == '__main__':
    ElixirApp().run()