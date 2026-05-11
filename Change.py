import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless=new')
driver = uc.Chrome(options=chrome_options)

class Change:
    def __init__(self, usd, rate_amd, rate_ru, rate_eur):
        self.usd = usd
        self.rate_amd = rate_amd
        self.rate_ru = rate_ru
        self.rate_eur = rate_eur
    def usd_to_amd(self):
        return round((self.usd * self.rate_amd),2)
    def usd_to_rub(self):
        return round((self.usd * self.rate_ru),2)
    def usd_to_eur(self):
        return round((self.usd * self.rate_eur),2)
         
try:
    driver.get(url='https://www.rate.am/hy/armenian-dram-exchange-rates/banks')
    
    kurs_amd = driver.find_element(By.XPATH, '/html/body/div[2]/main/div/div[1]/div[1]/div/div[2]/div[2]/div/div[1]/div[2]/div[2]').text
    kurs_ru = driver.find_element(By.XPATH, '/html/body/div[2]/main/div/div[1]/div[1]/div/div[2]/div[2]/div/div[14]/div[2]/div[2]').text

    clean_amd = kurs_amd.replace(',', '').strip()
    clean_ru = kurs_ru.replace(',', '').strip()
    
    converter = Change(usd=int(input('Enter usd count: ')), rate_amd=float(clean_amd), rate_ru=float(clean_ru), rate_eur=1.2)
    
    print(converter.usd_to_amd())
    print(converter.usd_to_rub())
    print(converter.usd_to_eur())
    
except Exception as ex:
    print(ex.__class__.__name__)    
    
finally:
    driver.quit()
