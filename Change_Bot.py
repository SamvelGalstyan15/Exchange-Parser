import os
import requests
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from kaggle_secrets import UserSecretsClient 

user_secrets = UserSecretsClient()
TOKEN = user_secrets.get_secret("TELEGRAM_TOKEN")
CHAT_ID = user_secrets.get_secret("TELEGRAM_CHAT_ID")

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

chrome_options.binary_location = "/usr/bin/google-chrome"
driver = uc.Chrome(
    options=chrome_options, 
    browser_executable_path="/usr/bin/google-chrome"
)

class Change:
    def __init__(self, usd, rate_amd, rate_ru, rate_eur):
        self.usd = usd
        self.rate_amd = rate_amd
        self.rate_ru = rate_ru
        self.rate_eur = rate_eur

    def usd_to_amd(self):
        return round((self.usd * self.rate_amd), 2)
    def usd_to_rub(self):
        return round((self.usd * self.rate_ru), 2)
    def usd_to_eur(self):
        return round((self.usd * self.rate_eur), 2)

try:
    driver.get(url='https://rate.am')
    driver.implicitly_wait(10) 

    kurs_amd = driver.find_element(By.XPATH, '/html/body/div[2]/main/div/div[1]/div[1]/div/div[2]/div[2]/div/div[1]/div/div[2]/div[2]').text
    kurs_ru = driver.find_element(By.XPATH, '/html/body/div[2]/main/div/div[1]/div[1]/div/div[2]/div[2]/div/div[14]/div/div[2]/div[2]').text

    clean_amd = kurs_amd.replace(',', '').strip()
    clean_ru = kurs_ru.replace(',', '').strip()

    usd_amount = int(input('Enter usd count: '))
    converter = Change(usd=usd_amount, rate_amd=float(clean_amd), rate_ru=float(clean_ru), rate_eur=1.2)

    res_amd = converter.usd_to_amd()
    res_rub = converter.usd_to_rub()
    res_eur = converter.usd_to_eur()

    print(f"AMD: {res_amd}")
    print(f"RUB: {res_rub}")
    print(f"EUR: {res_eur}")

    if TOKEN and CHAT_ID:
        message = f"💰 Конвертация {usd_amount}$:\n🇦🇲 AMD: {res_amd}\n🇷🇺 RUB: {res_rub}\n🇪🇺 EUR: {res_eur}"
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        requests.post(url, data={"chat_id": CHAT_ID, "text": message})

except Exception as ex:
    print(f"Ошибка: {ex}")

finally:
    driver.quit()
