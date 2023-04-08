from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time



def chrome_driver():
    #layanan chromedriver
    service = Service(executable_path="/path/to/chromedriver")

    #setting chromedriver
    chrome_options = Options()
    prefs = {"download.default_directory":r"C:\Users\inas\Downloads\PHYTON\program_python\download sfile"}
    chrome_options.add_experimental_option("prefs",prefs)

    global driver
    driver = webdriver.Chrome(service=service, options=chrome_options)
    url = f'https://sfile.mobi/search.php?q={search}&search=Search'
    driver.get(url)
    driver.refresh()


search = input('cari: ')
x = int(input('masukkan urutan (1/2/3): '))
y = int(input('banyak data ingin di download: '))

data = x + y
while x < data:
    chrome_driver()
    try:
        time.sleep(5)
        click = driver.find_element(By.XPATH, f'/html/body/div[2]/div/div[1]/div[{x+1}]/a').click()
        time.sleep(10)
    except:
        chrome_driver()
        time.sleep(5)
        click = driver.find_element(By.XPATH, f'/html/body/div[2]/div/div[1]/div[{x+1}]/a').click()
        time.sleep(10)

    try:
        download = driver.find_element(By.ID, 'download').click()
        time.sleep(10)
        driver.quit()
    except:
        try:
            chrome_driver()
            click = driver.find_element(By.XPATH, f'/html/body/div[2]/div/div[1]/div[{x+2}]/a').click()
            time.sleep(10)
            download = driver.find_element(By.ID, 'download').click()
            time.sleep(10)
            driver.quit()
        except:
            chrome_driver()
            click = driver.find_element(By.XPATH, f'/html/body/div[2]/div/div[1]/div[{x+3}]/a').click()
            time.sleep(10)
            download = driver.find_element(By.ID, 'download').click()
            time.sleep(10)
            driver.quit()



    x += 1