from kivy.app import App
from kivy.uix.popup import Popup
from kivy.config import Config
from kivy.uix.button import Button
from kivy.uix.widget import Widget

from corona_leb import coronaLeb


#   print(coronaLeb().corona_dict['recovered'])
#   str(coronaLeb().corona_dict[""])


class MyGrid(Widget):

    def __init__(self, **kwargs):   #initial method
        super(MyGrid, self).__init__(**kwargs)   #defining a parent class
        self.change_text()   #calling the method to change the text

    def change_text(self):   #defining a method that will update the text in the app
        self.ids.update_date.text = "Last Update: " + str(coronaLeb().corona_dict["update date"])   #for each specific id defined in the kv file the text will be updated depending on the data storred in the disctionnary
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

    title = "Corona Lebanon"   #setting the window title

    Config.set('graphics', 'width', '400')   #setting the window dimensions
    Config.set('graphics', 'height', '600')
    
    def build(self):
        return MyGrid()   #calling the class that will build the app


if __name__=="__main__":
    MyApp().run()   #running the app to open the window
