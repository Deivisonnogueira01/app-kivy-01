from kivy.app import App
from kivy.uix.widget import Widget


class SalaWidget(Widget):
    pass

class MySala(App):
    def build(self):
        return SalaWidget()

if __name__ == '__main__' :
    MySala().run()       