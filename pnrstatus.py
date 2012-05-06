import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def close_all_popups(driver):
#    time.sleep(0.5)
#    print "close_all_popups", 
    driver.window_handles
    for h in driver.window_handles[1:]:
#        print "closing", repr(h)
        driver.switch_to_window(h)
        driver.close()
    driver.switch_to_window(driver.window_handles[0])
#main
#    get_pnrstatus
#    read_pnrstatus            

def main(pnr_no):

    driver = webdriver.Firefox()
    driver.get("http://www.indianrail.gov.in/")
    #driver.get("http://indianrail.gov.in/pnr_Enq.html")
    close_all_popups(driver)
    driver.find_element_by_partial_link_text("PNR Status").click()
    close_all_popups(driver)


    #pnr_no = '4140576839'
    pnr_field = driver.find_element_by_name('lccp_pnrno1')
    pnr_field.send_keys(pnr_no + Keys.RETURN)
    close_all_popups(driver)

    
    elements = driver.find_element_by_id("center_table").find_elements_by_tag_name("td")
    for (i, ele) in enumerate(elements[:-1]):
        if i%3==0:
            print
        print repr(ele.text),

    #for ele in elements[:-1]:
    #    ele.text
    #driver.close()

if __name__ == "__main__":
   main(sys.argv[1])



