
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import pandas as pd
from datetime import datetime
import os
import sys

#app_path = os.path.dirname(sys.executable)

datenow = datetime.now()
year_month_day = datenow.strftime("%Y%m%d") #YYYYMMDD

website = "https://www.skysports.com/football"
path = "/Users/foodpanda-gary/Documents/Github/python_repo/chromedriver"

#headless mode
options = Options()
options.headless = True

service = Service(executable_path=path)

driver = webdriver.Chrome(service=service, options=options)

driver.implicitly_wait(10)
driver.get(website)

driver.switch_to.frame("sp_message_iframe_658052")
driver.find_element(by="xpath", value='//button[@title="Accept all"]').click()
driver.switch_to.default_content()

containers = driver.find_elements(by="xpath", value='//div[@class="news-list__body"]')

titles_list = []
subtitles_list = []
links_list = []

for container in containers:
    title = container.find_element(by="xpath", value='./h4/a').text
    subtitle = container.find_element(by="xpath", value='./p').text
    link = container.find_element(by="xpath", value='./h4/a').get_attribute("href")

    titles_list.append(title)
    subtitles_list.append(subtitle)
    links_list.append(link)

scrap_dict = {'title': titles_list, 'subtitle':subtitles_list, 'link':links_list}

df_headlines = pd.DataFrame(scrap_dict)
file_name = f'skysports_headlines_{year_month_day}.csv'
#final_path = os.path.join(app_path, file_name)

df_headlines.to_csv(file_name)

driver.quit()