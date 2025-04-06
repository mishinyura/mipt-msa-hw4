from abc import ABC, abstractmethod

class CurrencyRateProvider(ABC):
    @abstractmethod
    def get_rates(self):
        pass

class CurrencyConverter(ABC):
    @abstractmethod
    def convert(self, amount):
        pass