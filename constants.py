import os
from dotenv import load_dotenv
import sys
load_dotenv()

TG_TOKEN = os.getenv("TOKEN")
DB_PATH = "data.db"

if sys.platform.startswith("win"):

    CHROMEDRIVER_PATH = "./chromedriver-win64/chromedriver.exe"
else:
    CHROMEDRIVER_PATH = "./chromedriver-linux64/chromedriver"

