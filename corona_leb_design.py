from kivy.app import App
from kivy.uix.popup import Popup
from kivy.config import Config
from kivy.uix.button import Button
from kivy.uix.widget import Widget

from corona_leb import coronaLeb


#   print(coronaLeb().corona_dict['recovered'])
#   str(coronaLeb().corona_dict[""])


class MyGrid(Widget):

    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.change_text()

    def change_text(self):
        self.ids.update_date.text = "Last Update: " + str(coronaLeb().corona_dict["update date"])
        self.ids.daily_cases.text = str(coronaLeb().corona_dict["daily cases"])
        self.ids.tests.text = "Tests:" + str(coronaLeb().corona_dict["daily tests"])


class MyApp(App):

    title = "Corona Lebanon"

    Config.set('graphics', 'width', '400')
    Config.set('graphics', 'height', '600')
    
    def build(self):
        return MyGrid()


if __name__=="__main__":
    MyApp().run()
