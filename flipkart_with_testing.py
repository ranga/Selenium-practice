from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def search(section, query):
    # click on section dropdown
    driver.find_element_by_id("fk-menuSelIcon").click()

    # get all options
    elems = driver.find_element_by_id("fk-mI").find_elements_by_class_name("line")
    for e in elems:
        print e.text
        if e.text == section:
            e.click()
            break

    e = driver.find_element_by_id("fk-top-search-box")
    e.clear()
    e.send_keys(query)    
    e.send_keys(Keys.RETURN)
   # driver.find_element_by_id("fk-top-search-box").send_keys(Keys.RETURN) 
 
driver = webdriver.Firefox()
driver.get("http://www.flipkart.com/")

search("Books", "8184110561")

# to select first result
#driver.find_element_by_css_selector(".fk-srch-item h2 a").click()
#search("Cameras", "Powershot")

#testing details with ISBN
expecting_values = {'Book': 'Techniques of Teaching Economics'}
details = driver.find_element_by_id("details")
'''
even_rows = details.find_element_by_class_name("even")
odd_rows = details.find_element_by_class_name("odd")
book_name = odd_rows.find_element_by_class_name('specs-value').text

if book_name == expecting_values['Book']:
    print 'book name test passed' 


even_rows = details.find_elements_by_class_name("even")
odd_rows = details.find_elements_by_class_name("odd")
for row in odd_rows:
    field_text = row.find_element_by_class_name('specs-value').text
    print field_text

for row in even_rows:
    field_text = row.find_element_by_class_name('specs-value').text
    print field_text
'''
rows = details.find_elements_by_tag_name("td")

for row in rows:
    print row.text.strip()

"""
e = driver.find_element_by_id("fk-mI")

print e
print e.find_elements_by_class_name("line")

#[e for e in lines if e.text == 'Cameras'][0].click(0)
"""
time.sleep(5)
driver.close()

