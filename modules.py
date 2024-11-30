import requests

class CurrencyConverter:
    def __init__(self, api_urls):
        self.api_urls = api_urls
        self.rates = {}

    def fetch_rates(self):
        for currency, url in self.api_urls.items():
            response = requests.get(url)
            if response.status_code == 200:
                self.rates[currency] = response.json().get('rates', {})
            else:
                raise Exception(f"Error fetching exchange rates for {currency}")

    def convert(self, amount, from_currency, to_currency):
        if from_currency == to_currency:
            return amount

        # Handle missing rates gracefully
        if from_currency not in self.rates['USD'] or to_currency not in self.rates['USD']:
            raise Exception(f"Rates not available for {from_currency} or {to_currency}")

        if from_currency == 'USD':
            base_amount = amount
        else:
            base_amount = amount / self.rates['USD'].get(from_currency, 1)

        if to_currency == 'USD':
            return base_amount

        return base_amount * self.rates['USD'].get(to_currency, 1)
