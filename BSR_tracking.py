from selenium import webdriver
import time, json, os
from datetime import datetime


class BestSellerRankTracker:

    def __init__(self, browser, product_urls):
        self.br = browser
        self.urls = product_urls
    
    def get_BSR(self):
        for product, url in self.urls.items():

            JSON_file_path = f"{product}.json"
            actual_date = datetime.now().strftime("%d-%m-%Y")
            
            try:
                with open(JSON_file_path) as f:
                    data = json.load(f)
            except FileNotFoundError:
                data = dict()
                data[actual_date] = []
            
            # open product page
            self.br.get(url)

            # retrieve the text containing the BSR
            while True:    
                try:
                    text = self.br.find_element_by_xpath('//*[@id="productDetails_detailBullets_sections1"]/tbody/tr[3]/td/span/span[1]').text
                    break
                except Exception as e:
                    delay += 1
                    print(type(e).__name__)

            # add the BSR to the json file
            BSR = int(text.replace(',', '').split()[1])
            print(f"BSR of {product} is {BSR}")
            data[actual_date].append({"Time": datetime.now().strftime("%H:%M:%S"), "BSR": BSR})

            with open(JSON_file_path, 'w') as f:
                json.dump(data, f, indent=2)

        


# make the webdriver works in the background
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")

BROWSER = webdriver.Chrome('C:/Users/gedeo/OneDrive/Documenti/Python/chromedriver.exe', options=chrome_options)
PRODUCT_URLS = {
                "BidMamba": 'https://www.amazon.it/gp/product/B08F7QCT8M', 
                "DEKOVITA": 'https://www.amazon.it/Dekovita-vaso-portaoggetti-Set-decorativo/dp/B078XGBKPR',
                }

tracker = BestSellerRankTracker(BROWSER, PRODUCT_URLS)
while True:
    tracker.get_BSR()
    time.sleep(5)

# close Chrome window
tracker.br.quit()
