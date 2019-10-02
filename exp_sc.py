from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time
import datetime
#import smtplib
#from email.mime.multipart import MIMEMultipart

class ExpediaDriver():

    def __init__(self):
        """
        eine Klasse die eine Driver Anfrage darstellt
        """
        self.driver = webdriver.Chrome(executable_path='/Users/Fabi/Downloads/chromedriver')
        self.df = pd.DataFrame()
        self.dep_times_list = []
        self.arr_times_list = []
        self.airlines_list = []
        self.price_list = []
        self.durations_list = []
        self.stops_list = []
        self.layovers_list = []

    def ticket_chooser(self, ticket):

        try:

            ticket_type = self.driver.find_element_by_xpath(ticket)

            ticket_type.click()

        except Exception as e:

            pass

    def dep_country_chooser(self, dep_country):

        fly_from = self.driver.find_element_by_xpath("//input[@id='flight-origin-hp-flight']")

        time.sleep(1)

        fly_from.clear()

        time.sleep(.5)

        fly_from.send_keys('  ' + dep_country)

        time.sleep(.7)

        first_item = self.driver.find_element_by_xpath("//a[@id='aria-option-0']")

        time.sleep(1.5)

        first_item.click()

    def arrival_country_chooser(self, arrival_country):

        fly_to = self.driver.find_element_by_xpath("//input[@id='flight-destination-hp-flight']")

        time.sleep(1)

        fly_to.clear()

        time.sleep(1.5)

        fly_to.send_keys('  ' + arrival_country)

        time.sleep(1.5)

        first_item = self.driver.find_element_by_xpath("//a[@id='aria-option-0']")

        time.sleep(1.5)

        first_item.click()

    def dep_date_chooser(self, dep_date):
        month, day, year = dep_date

        dep_date_button = self.driver.find_element_by_xpath("//input[@id='flight-departing-hp-flight']")

        dep_date_button.clear()

        dep_date_button.send_keys(month + '/' + day + '/' + year)

    def return_date_chooser(self, return_date):

        month, day, year = return_date

        return_date_button = self.driver.find_element_by_xpath("//input[@id='flight-returning-hp-flight']")

        for i in range(11):

            return_date_button.send_keys(Keys.BACKSPACE)

        return_date_button.send_keys(month + '/' + day + '/' + year)

    def search(self):

        search = self.driver.find_element_by_xpath("//button[@class='btn-primary btn-action gcw-submit']")

        search.click()

        time.sleep(15)

        print('Results ready!')

    def compile_data(self):

        #departure times

        dep_times = self.driver.find_elements_by_xpath("//span[@data-test-id='departure-time']")

        self.dep_times_list = [w_elem.text for w_elem in dep_times] # das ist eine list-comprehension schreibweise

        #arrival times

        arr_times = self.driver.find_elements_by_xpath("//span[@data-test-id='arrival-time']")

        self.arr_times_list = [value.text for value in arr_times]

        #airline name

        airlines = self.driver.find_elements_by_xpath("//span[@data-test-id='airline-name']")

        self.airlines_list = [value.text for value in airlines]

        #prices

        prices = self.driver.find_elements_by_xpath("//span[@data-test-id='listing-price-dollars']")

        for value in prices:
            self.price_list.append(value.text.strip('$'))


        #durations

        durations = self.driver.find_elements_by_xpath("//span[@data-test-id='duration']")

        self.durations_list = [value.text for value in durations]

        #stops

        stops = self.driver.find_elements_by_xpath("//span[@class='number-stops']")

        self.stops_list = [value.text for value in stops]

        #layovers

        layovers = self.driver.find_elements_by_xpath("//span[@data-test-id='layover-airport-stops']")

        self.layovers_list = [value.text for value in layovers]

        now = datetime.datetime.now()

        current_date = (str(now.year) + '-' + str(now.month) + '-' + str(now.day))

        current_time = (str(now.hour) + ':' + str(now.minute))

        current_price = 'price' + '(' + current_date + '---' + current_time + ')'

# Excel Ausgabe (Felder für Excel werden befüllt)

        for i in range(len(self.dep_times_list)):

            try:

                self.df.loc[i, 'departure_time'] = self.dep_times_list[i]

            except Exception as e:

                pass

            try:

                self.df.loc[i, 'arrival_time'] = self.arr_times_list[i]

            except Exception as e:

                pass

            try:

                self.df.loc[i, 'airline'] = self.airlines_list[i]

            except Exception as e:

                pass

            try:

                self.df.loc[i, 'duration'] = self.durations_list[i]

            except Exception as e:

                pass

            try:

                self.df.loc[i, 'stops'] = self.stops_list[i]

            except Exception as e:

                pass

            try:

                self.df.loc[i, 'layovers'] = self.layovers_list[i]

            except Exception as e:

                pass

            try:

                self.df.loc[i, str(current_price)] = self.price_list[i]

            except Exception as e:

                pass

        print('Excel Sheet Created!')

container = [
    dict(departure="Stuttgart", arrival="Mexico", dep_date=('01', '01', '2020'), ret_date=('01', '11', '2020')),
    dict(departure="Stuttgart", arrival="Mexico", dep_date=('01', '01', '2020'), ret_date=('01', '11', '2020')),
    {'departure':"Frankfurt", 'arrival':"Mexico", 'dep_date':('01', '01', '2020'),'ret_date':('01', '11', '2020')},
    {'departure':"München", 'arrival':"Mexico", 'dep_date':('01', '01', '2020'),'ret_date':('01', '11', '2020')},
]

writer = pd.ExcelWriter("flights.xlsx")

for i, flight_dict in enumerate(container):

    driver = ExpediaDriver() # Hier wird das erste mal die __init__() ausgeführt

    # Setting ticket types paths

    return_ticket = "//label[@id='flight-type-roundtrip-label-hp-flight']"

    one_way_ticket = "//label[@id='flight-type-one-way-label-hp-flight']"

    multi_ticket = "//label[@id='flight-type-multi-dest-label-hp-flight']"

    departure = flight_dict['departure']
    arrival = flight_dict['arrival']
    dep_date = flight_dict["dep_date"]
    ret_date = flight_dict["ret_date"]

    link = 'https://www.expedia.com/'

    driver.driver.get(link)

    time.sleep(5)

    #choose flights only

    flights_only = driver.driver.find_element_by_xpath("//button[@id='tab-flight-tab-hp']")

    flights_only.click()

    driver.ticket_chooser(return_ticket) 

    driver.dep_country_chooser(departure)

    driver.arrival_country_chooser('Mexico')

    driver.dep_date_chooser(dep_date)

    driver.return_date_chooser(ret_date)

    driver.search()

    driver.compile_data()

    driver.df.to_excel(writer, sheet_name=f'{departure}_{i}')

    driver.driver.close()

writer.save()

################# 

#     #save values for email
#
#     #current_values = driver.df.iloc[0]
#
#     #cheapest_dep_time = current_values[0]
#
#     #cheapest_arrival_time = current_values[1]
#
#     #cheapest_airline = current_values[2]
#
#     #cheapest_duration = current_values[3]
#
#     #cheapest_stops = current_values[4]
#
#     #cheapest_price = current_values[-1]
#
#     #print('run {} completed!'.format(i))
#
