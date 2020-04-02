from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time

option = webdriver.ChromeOptions()
option.add_argument(" — incognito")

# Give the path of the chrome driver downloaded on your local machine
browser = webdriver.Chrome('/Users/raj.g/Downloads/chromedriver')

browser.get("https://play.google.com/store/apps/details?id=org.jfedor.frozenbubble&hl=en_US&showAllReviews=true")


def scroll_down():
    """A method for scrolling the page."""
    
    # Get scroll height.
    last_height = browser.execute_script("return document.body.scrollHeight")
    
    while True:
        
        # Scroll down to the bottom.
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
        # Wait to load the page.
        time.sleep(2)
        
        # Calculate new scroll height and compare with last scroll height.
        new_height = browser.execute_script("return document.body.scrollHeight")
        
        if new_height == last_height:
            break
        
        last_height = new_height


reviewer_name = browser.find_elements_by_xpath("//span[@class='X43Kjb']")

for x in reviewer_name:
    while len(reviewer_name) < 400:
        scroll_down()
        reviewer_name = browser.find_elements_by_xpath("//span[@class='X43Kjb']")
reviews = browser.find_elements_by_xpath("//div[@class='zc7KVe']")
print("RATING\tREVIEWER NAME\tREVIEW DATE\tREVIEW TEXT\tDEVELOPER NAME\tRESPONSE DATE\tDEVELOPER RESPONSE")
for reviewEle in reviews:
    try:
        developer_responses = reviewEle.find_element_by_xpath(".//div[@class='LVQB0b']")
    except NoSuchElementException:
        continue
    if developer_responses:
        reviewer_name = reviewEle.find_element_by_xpath(".//span[@class='X43Kjb']")
        reviewer_time = reviewEle.find_element_by_xpath(".//span[@class='p2TkOb']")
        rating = reviewEle.find_element_by_xpath(".//div[@class='pf5lIe']").find_element_by_css_selector('div').get_attribute('aria-label')
        reviews_content = reviewEle.find_element_by_xpath(".//span[@jsname='bN97Pc']")
        response_time = developer_responses.find_element_by_xpath(".//span[@class='p2TkOb']")
        response_developer = developer_responses.find_element_by_xpath(".//span[@class='X43Kjb']")
        review = reviewEle.find_element_by_xpath(".//span[@jsname='bN97Pc']")
        print(
            rating + "\t" + reviewer_name.text + "\t" + reviewer_time.text + "\t" + review.text + "\t" + response_developer.text + "\t" + response_time.text + "\t" + developer_responses.text.split("\n")[1])
