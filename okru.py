from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os

#instalare si configurare chromedriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
browser = webdriver.Chrome('chromedriver',chrome_options=chrome_options)

#open the web page
url = "https://ok.ru/video/c5317365" #trebuie editat url-ul canalului
#browser = webdriver.Chrome()
browser.get(url)

#scroll down the page to load all the videos
#scroll down 1000 pixels each time
SCROLL_PAUSE_TIME = 0.5

# Get scroll height
last_height = browser.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = browser.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

#get the links and titles
links = browser.find_elements(By.XPATH, "//div[starts-with(@id, 'video-card_img_')]//a[@aria-label='Vizualizează']")
titles = browser.find_elements(By.XPATH,"//a[contains(@title, 'Doctor Quinn')]") #trebuie editat cu numele canalului

#create the folder
folder_name = 'Doctor Quinn' #trebuie editat cu numele canalului
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

#create .strm file for each video
for i in range(len(links)):
    link = links[i].get_attribute("href").split('?')[0]
    #title = titles[i].text
    title = titles[i].get_attribute('title')
    file_name = title.replace("/", " ") + ".strm"
    file_path = os.path.join(folder_name, file_name)
    with open(file_path, "w") as file:
        file.write(link)

#close the browser
browser.close()
