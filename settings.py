import os

from dotenv import load_dotenv

load_dotenv(".env")

TOKEN = os.getenv("TOKEN")
API_KEY_EXCHANGE = os.getenv("API_KEY_EXCHANGE")

# Валюты для обмена
CURRENCIES = ["EUR", "RUB", "GBP", "CNY", "USD"]
