import requests
from bs4 import BeautifulSoup

class CurrencyConverter:
    def __init__(self):
        self.usd_to_uah_rate = None
        self.update_exchange_rate()
    def update_exchange_rate(self):
        url = 'https://bank.gov.ua/ua/markets/exchangerates'
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            table = soup.find('table', {'class': 'table'})
            if table:
                rows = table.find_all('tr')
                for row in rows:
                    cols = row.find_all('td')
                    if len(cols) > 4 and cols[1].text.strip() == 'USD':
                        self.usd_to_uah_rate = float(cols[4].text.replace(',', '.'))
                        break
            if self.usd_to_uah_rate is None:
                print("нема тут доларів, америкоси всьо.")
        else:
            print(f"нбу проти цього: {response.status_code}")
    def convert_uah_to_usd(self):
        if self.usd_to_uah_rate is None:
            print("не.")
            return
        try:
            amount_uah = float(input("скіко грн "))
            amount_usd = amount_uah / self.usd_to_uah_rate
            print(f"{amount_uah} гіріні = {amount_usd:.2f} дола дола")
        except ValueError:
            print("норм циферкі клацни .")
converter = CurrencyConverter()
converter.convert_uah_to_usd()
