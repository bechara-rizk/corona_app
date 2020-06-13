from kivy.app import App
from kivy .uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.config import Config
from kivy.uix.button import Button

from corona_leb import coronaLeb


print(coronaLeb().corona_dict['recovered'])


class myFloatLayout():

    def button_pressed(self):
        print("pressed")
        



class coronaApp(App):

    Config.set('graphics', 'width', '300')
    Config.set('graphics', 'height', '600')

    title = "Corona Lebanon"

    def build(self):
        return myFloatLayout()



if __name__=="__main__":
    coronaApp().run()