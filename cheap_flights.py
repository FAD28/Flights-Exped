from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time
from copy import copy
import datetime

print("")
print("Ziel ist es diese Seiten zu Scrapen: ")
print("# LINKS:https://www.tuifly.com/flugangebote "
      "https://www.kayak.de/flugangebote")
time.sleep(3)
# LINKS:
# https://www.tuifly.com/flugangebote?tts=GVABCNc~20191119-VY6198-NonX3~20191126-VY6201-NonX3|STRPMIc~20191201-X32172-X3Pure~20191208-VY3440-NonX3
# https://www.tuifly.com/flugangebote
# https://www.kayak.de/flugangebote
# https://www.statravel.de/aktuelle-flugangebote.htm
# https://www.lufthansa.com/de/de/fluege
df = pd.DataFrame
# self.tui_dep_time = []
# self.tui_ret_time = []
# Listen bsp: self.dep_times_list = []

def compile_data_tui():
    j = 0
    while j < 61:
        j += 1
        try:

            t_destiny = driver.find_elements_by_xpath( f"/html/body/div[2]/main/section[2]/div/div/div[3]/div[{j}]/label[1]/div[2]/div[1]/span[2]")
            tui_destiny = [element.text for element in t_destiny]
            print(" Ziel ")
            print(tui_destiny)

            t_price = driver.find_elements_by_xpath(f"/html/body/div[2]/main/section[2]/div/div/div[3]/div[{j}]/label[1]/div[2]/div[2]/div")
            tui_price = [element.text for element in t_price]
            print(tui_price)

            t_departure = driver.find_elements_by_xpath(f"/html/body/div[2]/main/section[2]/div/div/div[3]/div[{j}]/label[1]/div[2]/div[1]/span[1]")
            tui_departure = [element.text for element in t_departure]
            print("Abflugort ist: ")
            print(tui_departure)

        except:
            print("Konnte nicht durchgeführt werden")
            pass

def tui_chooser():
    i = 0
    while i < 61:
        try:
            i += 1
            try:
                show_more = driver.find_element_by_xpath(f"/html/body/div[2]/main/section[2]/div/div/div[3]/div[{i}]/label[2]")
                show_more.click()
                time.sleep(3)
                # driver.execute_script("window.scrollTo(500, 1000)")
                time.sleep(3)
            except:
                # print("jetzt wird nach css gesucht")
                show_more2 = driver.find_element_by_css_selector(f"body > div.page.underlay-spacer.js-underlay-spacer > main > section.box > div > div > div.js-trip-tile-list > div:nth-child({i}) > label.trip-tile__button")
                driver.execute_script("arguments[0].click();", show_more2)
        except:
            print("Alles wurde geöffnet")

########################################################################################################################

########################################################################################################################


def kayak_chooser():
    time.sleep(3)
    try:
        cookies_kacke = driver.find_element_by_xpath('/html/body/div[6]/div/div[3]/div/div/div/div/div[1]/div/div[2]/div[2]/div[2]/button')
        print(" C1 ")

    except:
        cookies_kacke = driver.find_element_by_css_selector('#d9Mu-cookie-consent-dialog-body > div > div > div.page-1._i57._jht._jhn > div > div._iEG._itL > div._iaB._iDa > div._iEG')
        print(" C2 ")

    webdriver.ActionChains(driver).move_to_element(cookies_kacke).click(cookies_kacke).perform()

    time.sleep(5)
    print("Mehr anzeigen")
    time.sleep(2)
    for i in range(2):
        time.sleep(2)
        driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/main/div/div[1]/div/div[2]/div/div/div[3]/div[2]/div/span').click()

# Mehr Ergebnisse:
# /html/body/div[1]/div/div[1]/main/div/div[1]/div/div[2]/div/div/div[3]/div[2]/div/span

def compile_data_kayak():
    k = 0
    while k < 15:
        k += 1
        print(k)
        try:
            k_price = driver.find_elements_by_xpath(f'/html/body/div[1]/div/div[1]/main/div/div[1]/div/div[2]/div/div/div[3]/div[2]/div/div[1]/div/div[{k}]/div/a/div[7]/div[2]') # "//div[@class='price']"    /// f"/html/body/div[1]/div/div[1]/main/div/div[1]/div/div[2]/div/div/div[3]/div[2]/div/div[1]/div/div[{k}]/div/a/div[7]/div[2]"
            kayak_price = [element.text for element in k_price]
            print(kayak_price)
        except:
            print("Kayak hat nicht funktioniert!")
            pass

        try:
            k_destiny = driver.find_elements_by_xpath(f'/html/body/div[1]/div/div[1]/main/div/div[1]/div/div[2]/div/div/div[3]/div[2]/div/div[1]/div/div[{k}]/div/a/div[5]')
            kayak_destiny = [element.text for element in k_destiny]
            print(kayak_destiny)

        except:
            print("Error")
            pass

        try:
            k_depart = driver.find_elements_by_xpath("/html/body/div[1]/div/div[1]/main/div/div[1]/div/div[2]/div/div/h2/span")
            kayak_departure = [element.text for element in k_depart]
            print(kayak_departure)

        except:
            print("Abflugort nicht da")
            pass

        try:
            # k_dates = driver.find_elements_by_xpath(f'/html/body/div[1]/div/div[1]/main/div/div[1]/div/div[2]/div/div/div[3]/div[2]/div/div[1]/div/div[{k}]/div/a/div[3]')
            k_dates = driver.find_elements_by_xpath('')
            print(k_dates)
            kayak_dates = [element.text for element in k_dates]
            print(kayak_dates)

        except:
            print("Keine Daten gefunden")
            pass


# /html/body/div[1]/div/div[1]/main/div/div[1]/div/div[2]/div/div/div[3]/div[2]/div/div[1]/div/div[1]/div/a/div[3]
# '//div[@class ="datesWrapper"]'
#//*[@id="MnWc"]
# #gaa2 > a > div.datesWrapper
# #Gi9A > a > div.datesWrapper
# #xKww > a > div.datesWrapper
# #iCZV > a > div.datesWrapper
# /html/body/div[1]/div/div[1]/main/div/div[1]/div/div[2]/div/div/div[3]/div[2]/div/div[1]/div/div[2]/div/a/div[3]
# /html/body/div[1]/div/div[1]/main/div/div[1]/div/div[2]/div/div/div[3]/div[2]/div/div[1]/div/div[1]/div/a/div[3]
# f'/html/body/div[1]/div/div[1]/main/div/div[1]/div/div[2]/div/div/div[3]/div[2]/div/div[1]/div/div[{k}]/div/a/div[3]'
# #v9T5 > a:nth-child(1) > div:nth-child(3)
#

links = ["https://www.tuifly.com/flugangebote", "https://www.kayak.de/flugangebote"] #,  "https://www.statravel.de/aktuelle-flugangebote.htm"

for item in links:
    chromedriver = "/Users/Fabi/Downloads/chromedriver"
    driver = webdriver.Chrome(chromedriver)
    print(item)
    time.sleep(2)
    driver.get(item)
    time.sleep(2)

    # TUI
    if item == links[0]:
        # tui_chooser()
        # time.sleep(3)
        print("**********************")
        # time.sleep(3)
        compile_data_tui()
    else:
        print("ist kein Tui-link")
        pass


    # KAYAK
    if item == links[1]:
        time.sleep(3)
        kayak_chooser()
        time.sleep(3)
        compile_data_kayak()
    else:
        print("ist kein kayak-link")
        pass
    # if item == links[3]:


    time.sleep(5)
    driver.close()
    time.sleep(2)
