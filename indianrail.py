import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


def get_available_trains(driver, src, dst, klass, date):
    #driver.find_element_by_partial_link_text("PNR Status").click()
    source_stations = driver.find_element_by_name("lccp_src_stncode").find_elements_by_tag_name('option')
    #print dir(elems)
    for ss in source_stations:
        if ss.text == src: 
            ss.click()
            break

    destination_stations = driver.find_element_by_name("lccp_dstn_stncode").find_elements_by_tag_name("option")
    for ds in destination_stations:
        if ds.text == dst:
            ds.click()
            break

    class_selection = driver.find_element_by_name("lccp_classopt").find_elements_by_tag_name("option")
    for cs in class_selection:
        if cs.text == klass:
            cs.click()
            break

    dd, mm, yyyy = date.split('-')
    
    day_element = driver.find_element_by_name("lccp_day")
    day_element.clear()
    day_element.send_keys(dd) 

    month_element = driver.find_element_by_name("lccp_month")
    month_element.clear()
    month_element.send_keys(mm) 

    month_element.send_keys(Keys.RETURN) 

def get_availablity(driver, train_number):
    available_train_detail = driver.find_elements_by_name("lccp_trndtl")
    for atd in available_train_detail:
        #print dir(atd)
        value = atd.get_attribute('value')
        if train_number in value:
            atd.click()
            break
    atd.send_keys(Keys.RETURN)

def get_driver(url):
    driver = webdriver.Firefox()
    driver.get(url)
    
    return driver


driver = webdriver.Firefox()
#driver.get("http://www.indianrail.gov.in/")
driver.get("http://indianrail.gov.in/pnr_Enq.html")
#driver.find_element_by_partial_link_text("PNR Status")

pnr_no = '4140576839'
element = driver.find_element_by_name("lccp_pnrno1")
element.send_keys(pnr_no + Keys.RETURN)

#driver.close()

#driver.get("http://www.indianrail.gov.in/")

imp_stations_url = "http://indianrail.gov.in/between_Imp_Stations.html"
get_driver(imp_stations_url) 

source = 'GUNTUR - GNT' 
destination = 'BANGALORE - SBC'
klass = 'SLEEPER CLASS' 
date = '30-05-2012'
get_available_trains(driver, source, destination, klass, date)


train_number = '18463'
get_attribute(driver, train_number)



"""
driver.find_element_by_partial_link_text("PNR Status").click()
selenium.selenium.close()

#selenium.selenium.select_window()#to close advertisement window
element = driver.find_element_by_id("elememt")
element.send_keys("4140576839" + Keys.RETURN)

#driver.find_element_by_partial_link_text("Train Between").click()
#driver.find_element_by_name("lccp_src_stncode")

#driver.find_element_by_xpath("//select[@name='lccp_src_stncode']")

driver.find_element_by_partial_link_text("Train Between Important Stations").click()
#driver.find.element_by_name("lccp_src_stncode")
print dir(driver)
sleep(60)
driver.switch_to_window('Advertisement')
driver.close()
"""
"""
time.sleep(60)

clear_element = driver.find_element_by_name("Reset")
clear_element.click()
"""

