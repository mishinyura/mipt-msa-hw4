from converters import CurrencyConverter
from converters.exchange_rate import BaseRateProvider

class UsdCnyConverter(CurrencyConverter):
    def __init__(self, rate_provider=None):
        self.rate_provider = rate_provider or BaseRateProvider()

    def convert(self, amount):
        rates = self.rate_provider.get_rates()
        return amount * rates['CNY']