#take lat/long from commandline
#open url of weather//get current temp from specified website

import webbrowser, sys
from selenium import webdriver

if len(sys.argv) > 1:
  lat = sys.argv[1] #gets all items on command line except the first one, which is our program name
  lon = sys.argv[2]
else:
  lat = '39.6758' #default to KMGW
  lon = '-79.857'
#instead you can probably find by element id and then send keys to the object and then find and submit the button object
#webbrowser.open('http://forecast.weather.gov/MapClick.php?lat=' + lat + '&lon=' + lon)
#linkElem = browser.find_element_by_link_text('Go')
#linkElem.click()

browser = webdriver.Chrome()
#browser.get('http://forecast.weather.gov/MapClick.php?lat=' + lat + '&lon=' + lon)
browser.get('http://forecast.weather.gov/')

try:
    tempEle = browser.find_element_by_id('inputstring')
    tempEle.clear()
    #print(tempEle.tag_name)
    tempEle.send_keys(' 26508, WV, USA') # appends & doesnt get rid of the auto-populated text of "Enter Location..."
    sub = browser.find_element_by_id('btnSearch')
    #sub.submit()
    tempEle.submit()
    #htmlEle = browser.find_element_by_tag_name('html')
    #tempEle.send_keys(Keys.END)
    print('finished search actions')
except:
    print('not able to find temperature element')
