import re
import time
import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import constants
from db_manager import DatabaseManager

logger = logging.getLogger(__name__)


class Parser:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

        self.service = Service(constants.CHROMEDRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.service, options=chrome_options)
        self.db = DatabaseManager()

    def _clean_price(self, price_text):
        try:
            price_text = re.sub(r"[^\d,.]", "", price_text)
            price_text = price_text.replace(",", ".")
            return float(price_text) if price_text else None
        except Exception as e:                                   # TODO improve errors handling
            logger.error(f"Неверный формат данных цены\n{e}")
            return None

    def get_prices(self):                     # TODO make async
        sites = self.db.get_sites()

        if not sites:
            return None

        prices = []
        wait = WebDriverWait(self.driver, 10)

        for title, url, xpath in sites:
            try:
                logger.info(f"Parsing {title}...\n")
                self.driver.get(url)
                element = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
                price_text = element.text.strip()
                price = self._clean_price(price_text)
                if price:
                    prices.append(price)

            except Exception as e:                                 # TODO improve errors handling
                logger.error(f"Ошибка при парсинге {url}: {e}")

        self.driver.quit()

        return round(sum(prices) / len(prices), 2) if prices else None
