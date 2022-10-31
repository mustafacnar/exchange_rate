def append_rates(exchange_rates, rate_date):
    currency_list = []
    for exchange_rate in exchange_rates:
        if exchange_rate.select_one('BanknoteBuying').text != '' and exchange_rate.select_one('BanknoteSelling').text != '':
            currency = dict(currency_abbreviation=exchange_rate.attrs['currencycode'],
                            exchange_rate_buying=float(exchange_rate.select_one('BanknoteBuying').text),
                            exchange_rate_selling=float(exchange_rate.select_one('BanknoteSelling').text),
                            exchange_rate_date=rate_date)
            currency_list.append(currency)
    return currency_list
