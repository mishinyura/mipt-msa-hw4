from converters.usd_eur_converter import UsdEurConverter
from converters.usd_gbp_converter import UsdGbpConverter
from converters.usd_rub_converter import UsdRubConverter
from converters.usd_cny_converter import UsdCnyConverter


def main():
    amount = int(input('Введите значение в USD: \n'))

    converters = {
        'RUB': UsdRubConverter(),
        'EUR': UsdEurConverter(),
        'GBP': UsdGbpConverter(),
        'CNY': UsdCnyConverter()
    }

    for currency, converter in converters.items():
        print(f"{amount} USD to {currency}: {converter.convert(amount)}")


if __name__ == "__main__":
    main()