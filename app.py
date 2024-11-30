from flask import Flask, render_template, request 
from modules import CurrencyConverter

app = Flask(__name__)

base_url = 'https://api.exchangerate-api.com/v4/latest/'

API_URLS = {
    'USD': base_url + 'USD',
    'GBP': base_url + 'GBP',
    'EUR': base_url + 'EUR'
}

# Assuming CurrencyConverter class is modified to accept api_urls argument
converter = CurrencyConverter(API_URLS)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    error = None
    if request.method == 'POST':
        amount = float(request.form.get('amount', 0))
        from_currency = request.form.get('from_currency')
        to_currency = request.form.get('to_currency')
        try:
            converter.fetch_rates()
            result = converter.convert(amount, from_currency, to_currency)
        except Exception as e:
            error = str(e)
    return render_template('index.html', result=result, error=error)

if __name__ == "__main__":
    app.run(debug=True)
