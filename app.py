from append_exchange_rate import append_rates
import requests
from bs4 import BeautifulSoup
from pprint import pprint

exchange_rate_xml = "https://www.tcmb.gov.tr/kurlar/today.xml"


def exchange_rates():
    exchange_rates_dict = dict()
    xml_data = None
    while not xml_data:
        try:
            xml_data = requests.get(exchange_rate_xml)
        except Exception as exp:
            print(exp)
    soup = BeautifulSoup(xml_data.content, "lxml", from_encoding='UTF-8')
    date_data = soup.find('tarih_date')
    date = date_data.attrs["tarih"]
    currency_rates = soup.find_all("currency")
    currency_list = append_rates(currency_rates, date)
    exchange_rates_dict["exchange_rates"] = currency_list
    pprint(exchange_rates_dict)
    return exchange_rates_dict


exchange_rates()
