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
        self.ids.tests.text = "Tests: " + str(coronaLeb().corona_dict["daily tests"])
        self.ids.locals_cases.text = str(coronaLeb().corona_dict["daily cases locals"])
        self.ids.arrivals_cases.text = str(coronaLeb().corona_dict["daily cases arrivals"])
        self.ids.total_cases_box.text = str(coronaLeb().corona_dict["total cases"])
        self.ids.total_locals_box.text = "Locals: " + str(coronaLeb().corona_dict["total cases locals"])
        self.ids.total_arrivals_box.text = "Arrivals: " + str(coronaLeb().corona_dict["total cases arrivals"])
        self.ids.active_cases_box.text = str(coronaLeb().corona_dict["active cases"])
        self.ids.deaths_box.text = str(coronaLeb().corona_dict["deaths"])
        self.ids.reco_cases_box.text = str(coronaLeb().corona_dict["recovered"])
        self.ids.lockdown_cases_box.text = str(coronaLeb().corona_dict["lockdown cases"])


class MyApp(App):

    title = "Corona Lebanon"

    Config.set('graphics', 'width', '400')
    Config.set('graphics', 'height', '600')
    
    def build(self):
        return MyGrid()


if __name__=="__main__":
    MyApp().run()
