from selenium import webdriver
import time


class BestSellerRankTracker:

    def __init__(self, browser, product_urls):
        self.br = browser
        self.urls = product_urls
    
    def get_BSR(self, delay=0):
        for product, url in self.urls.items():
            self.br.get(url)

            while True:    
                try:
                    time.sleep(delay)
                    text = self.br.find_element_by_xpath('//*[@id="productDetails_detailBullets_sections1"]/tbody/tr[3]/td/span/span[1]').text
                    BSR = int(text.replace(',', '').split()[1])
                    print(f"BSR of {product} is {BSR}")
                    break
                except Exception as e:
                    delay += 1
                    print(type(e).__name__)
        
        self.br.close()


# make the webdriver works in the background
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")

BROWSER = webdriver.Chrome('C:/Users/gedeo/OneDrive/Documenti/Python/chromedriver.exe', options=chrome_options)
PRODUCT_URLS = {
                "BidMamba": 'https://www.amazon.it/gp/product/B08F7QCT8M', 
                "DEKOVITA": 'https://www.amazon.it/Dekovita-vaso-portaoggetti-Set-decorativo/dp/B078XGBKPR',
                }

tracker = BestSellerRankTracker(BROWSER, PRODUCT_URLS)
tracker.get_BSR()

