from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import xlsxwriter

option = webdriver.ChromeOptions()
option.add_argument(" — incognito")

browser = webdriver.Chrome('D:\ChromeDriver\chromedriver.exe')

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
    while len(reviewer_name) < 200:
        scroll_down()
        reviewer_name = browser.find_elements_by_xpath("//span[@class='X43Kjb']")

reviewers = [x.text for x in reviewer_name]

reviews_content = browser.find_elements_by_xpath("//span[@jsname='bN97Pc']")
reviews = [x.text for x in reviews_content]

developer_responses = browser.find_elements_by_xpath("//div[@class='LVQB0b']")
responses = [x.text for x in developer_responses]

#print(reviewer_name)
#print('revewers:')
for x in reviews:
    print(x)
#print(len(reviewers))
#print(reviews)
#print(responses)

#workbook = xlsxwriter.Workbook('Project777_Results')
#worksheet = workbook.add_worksheet()

#row = 0

#for col,data in reviewers:
#    worksheet.write_column(row,col,data)

#workbook.close()