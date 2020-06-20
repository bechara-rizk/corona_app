from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.config import Config
from kivy.uix.button import Button
from kivy.uix.widget import Widget

from corona_leb import coronaLeb


print(coronaLeb().corona_dict['recovered'])


class MyGrid(Widget):
    pass


class MyApp(App):

    title = "Corona Lebanon"

    Config.set('graphics', 'width', '400')
    Config.set('graphics', 'height', '600')
    
    def build(self):
        return MyGrid()


if __name__=="__main__":
    MyApp().run()
