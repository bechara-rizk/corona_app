from lxml.html import fromstring
from requests import get
from re import sub


class coronaLeb:
    def __init__(self):   #initial method
        self.load_info()   #calling a method to refresh the information

    def load_info(self):   #defining a function that will refresh the information
        self.corona_dict={}   #defining an empty dictionary which will contain the data

        self.page = get("https://corona.ministryinfo.gov.lb")   #getting data from the html page
        self.page = fromstring(self.page.content)   #parsing the html page

        self.daily_cases = self.page.xpath("//h1[@class='s-counter s-counter']/text()")   #storing the contents of the specific class from the html page inside a list
        self.daily_cases = sub('[^0-9]', '', self.daily_cases[0])   #filtering the contents of a specific item in a list to only numbers (removing spaces and other clutter)
        self.corona_dict['daily cases'] = self.daily_cases   #adding the data inside the dictionary

        self.daily_cases_locals = self.page.xpath("//h1[@class='s-counter21 s-counter']/text()")
        self.daily_cases_locals = sub('[^0-9]', '', self.daily_cases_locals[0])
        self.corona_dict['daily cases locals']=self.daily_cases_locals

        self.daily_cases_arrivals = int(self.daily_cases) - int(self.daily_cases_locals)
        self.corona_dict['daily cases arrivals']=self.daily_cases_arrivals

        self.total_cases = self.page.xpath("//h1[@class='s-counter6 s-counter']/text()")
        self.total_cases = sub("[^0-9]", "", self.total_cases[0])
        self.corona_dict['total cases']=self.total_cases

        self.total_cases_arrivals = self.page.xpath("//h1[@class='s-counter22 s-counter']/text()")
        self.total_cases_arrivals = sub("[^0-9]", "", self.total_cases_arrivals[0])
        self.corona_dict['total cases arrivals']=self.total_cases_arrivals

        self.total_cases_locals = int(self.total_cases) - int(self.total_cases_arrivals)
        self.corona_dict['total cases locals']=self.total_cases_locals

        self.active_cases = self.page.xpath("//h1[@class='s-counter6 s-counter']/text()")
        self.active_cases = sub("[^0-9]", "", self.active_cases[1])   #if a class has multiple elements in the page they will all be stored in the list with different indexes
        self.corona_dict['active cases']=self.active_cases

        self.death_cases = self.page.xpath("//h1[@class='s-counter5 s-counter']/text()")
        self.death_cases = sub("[^0-9]", "", self.death_cases[1])
        self.corona_dict['deaths']=self.death_cases

        self.cured_cases = self.page.xpath("//h1[@class='s-counter5 s-counter']/text()")
        self.cured_cases = sub("[^0-9]", "", self.cured_cases[2])
        self.corona_dict['recovered']=self.cured_cases

        self.lockd_cases = self.page.xpath("//h1[@class='s-counter5 s-counter']/text()")
        self.lockd_cases = sub("[^0-9]", "", self.lockd_cases[3])
        self.corona_dict['lockdown cases']=self.lockd_cases

        self.critical_cases = self.page.xpath("//h1[@class='s-counter5 s-counter']/text()")
        self.critical_cases = sub("[^0-9]", "", self.critical_cases[0])
        self.corona_dict['critical cases']=self.critical_cases

        self.daily_cases_tests_locals = self.page.xpath("//h1[@class='s-counter10 s-counter']/text()")
        self.daily_cases_tests_locals = sub("[^0-9]", "", self.daily_cases_tests_locals[0])
        self.corona_dict['daily tests locals']=self.daily_cases_tests_locals

        self.daily_cases_tests_arrivals = self.page.xpath("//h1[@class='s-counter23 s-counter']/text()")
        self.daily_cases_tests_arrivals = sub("[^0-9]", "", self.daily_cases_tests_arrivals[0])
        self.corona_dict['daily tests arrivals']=self.daily_cases_tests_arrivals

        self.daily_cases_tests = int(self.daily_cases_tests_locals) + int(self.daily_cases_tests_arrivals)
        self.corona_dict['daily tests']=self.daily_cases_tests

        self.update_date = self.page.xpath("//strong/text()")
        self.update_date = self.update_date[0]
        self.update_date = self.update_date.strip()   #removing the unwanted spaces from the date
        self.corona_dict['update date'] = self.update_date

    def print_info(self):   #defining a method that will print the data storred
        self.printed_text = f"""    
Update : {self.corona_dict['update date']}

Daily cases : {self.corona_dict['daily cases']}  ({self.corona_dict['daily tests']} tests)
    Locals : {self.corona_dict['daily cases locals']}  ({self.corona_dict['daily tests locals']} tests)
    Arrivals : {self.corona_dict['daily cases arrivals']}  ({self.corona_dict['daily tests arrivals']} tests)

Total cases : {self.corona_dict['total cases']}
    Locals : {self.corona_dict['total cases locals']}
    Arrivals : {self.corona_dict['total cases arrivals']}

Active cases :{self.corona_dict['active cases']}
    Ciritical cases : {self.corona_dict['critical cases']} 

Deaths : {self.corona_dict['deaths']}

Recovered : {self.corona_dict['recovered']}

Lockdown cases : {self.corona_dict['lockdown cases']}
"""   #defining a variable that will add the data to a text

        print(self.printed_text)   #printing the text with the data added


if __name__ == "__main__":   
    coronaLeb().print_info()   #only print the text if the class is executed directly and not imported
