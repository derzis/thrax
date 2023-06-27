from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os

# Instalare și configurare chromedriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
browser = webdriver.Chrome(options=chrome_options)

p = 'plugin://plugin.video.sendtokodi/?'

# Deschide pagina web
url = "https://ok.ru/video/c5317365"  # Trebuie editat URL-ul canalului
browser.get(url)

# Derulează în jos pentru a încărca toate videoclipurile
# Derulează cu 1000 de pixeli de fiecare dată
SCROLL_PAUSE_TIME = 0.5

# Obține înălțimea derulării
last_height = browser.execute_script("return document.body.scrollHeight")

while True:
    # Derulează până jos
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Așteaptă încărcarea paginii
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculează noua înălțime a derulării și compar-o cu ultima înălțime
    new_height = browser.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

# Obține link-urile și titlurile
links = browser.find_elements(By.XPATH, "//div[@data-l='t,movie']//a[@tabindex='-1']")
titles = browser.find_elements(By.XPATH, "//a[contains(@title, 'Doctor Quinn')]")  # Trebuie editat cu numele canalului

# Creează folder-ul
folder_name = 'Doctor Quinn'  # Trebuie editat cu numele canalului
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

# Creează fișierul .strm pentru fiecare videoclip
for i in range(len(links)):
    link = links[i].get_attribute("href").split('?')[0]
    #print(link)
    title = titles[i].get_attribute('title')
    file_name = title.replace("/", " ") + ".strm"
    file_path = os.path.join(folder_name, file_name)
    with open(file_path, "w") as file:
        file.write(p+link)

# Închide browser-ul
browser.quit()
