import currencyapicom

from settings import API_KEY_EXCHANGE, CURRENCIES


async def get_currency_rate(base_currency: str, currencies):
    """Получение текущего курса"""
    client = currencyapicom.Client(API_KEY_EXCHANGE)
    currency_rate = client.latest(base_currency=base_currency, currencies=currencies)
    return currency_rate


async def convert_currency(amount: int, base_currency: str):
    """Конвертация"""
    converted = {}

    local_currency = CURRENCIES.copy()
    if base_currency in local_currency:
        local_currency.remove(base_currency)
        rate = await get_currency_rate(base_currency, local_currency)
        for currency, rate in rate["data"].items():
            converted[rate["code"]] = rate["value"] * amount

        return converted
