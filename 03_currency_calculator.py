import requests
import tkinter as tk
from tkinter import ttk


def convert_currency(from_curr: str, to_curr: str, amount_: str):
    from_curr = from_curr.upper()
    to_curr = to_curr.upper()

    text['state'] = 'normal'
    text.delete(0, tk.END)

    if from_curr in currencies and to_curr in currencies and amount_:
        try:
            amount_ = float(amount_)
        except ValueError:
            text.insert(0, 'Please enter a number.')
            text['state'] = 'readonly'
            return None

        response = requests.get(f'https://api.exchangerate-api.com/v4/latest/{from_curr}')
        exchange_rates = response.json()['rates']
        to_curr_rate = exchange_rates[to_curr]
        result = amount_ * to_curr_rate

        text.insert(0, f'Your amount in {to_curr}: {result:.2f}')
        text['state'] = 'readonly'

    else:
        if from_curr not in currencies:
            text.insert(0, 'Please enter a valid currency to convert from.')
        elif to_curr not in currencies:
            text.insert(0, 'Please enter a valid currency to convert to.')
        elif not amount_:
            text.insert(0, 'Please enter an amount.')

        text['state'] = 'readonly'
        return None


currencies = ['USD', 'EUR', 'BGN', 'GBP', 'AED', 'AFN', 'ALL', 'AMD', 'ANG', 'AOA', 'ARS', 'AUD', 'AWG', 'AZN', 'BAM',
              'BBD', 'BDT', 'BHD', 'BIF', 'BMD', 'BND', 'BOB', 'BRL', 'BSD', 'BTN', 'BWP', 'BYN', 'BZD', 'CAD', 'CDF',
              'CHF', 'CLP', 'CNY', 'COP', 'CRC', 'CUP', 'CVE', 'CZK', 'DJF', 'DKK', 'DOP', 'DZD', 'EGP', 'ERN', 'ETB',
              'FJD', 'FKP', 'FOK', 'GEL', 'GGP', 'GHS', 'GIP', 'GMD', 'GNF', 'GTQ', 'GYD', 'HKD', 'HNL', 'HRK', 'HTG',
              'HUF', 'IDR', 'ILS', 'IMP', 'INR', 'IQD', 'IRR', 'ISK', 'JEP', 'JMD', 'JOD', 'JPY', 'KES', 'KGS', 'KHR',
              'KID', 'KMF', 'KRW', 'KWD', 'KYD', 'KZT', 'LAK', 'LBP', 'LKR', 'LRD', 'LSL', 'LYD', 'MAD', 'MDL', 'MGA',
              'MKD', 'MMK', 'MNT', 'MOP', 'MRU', 'MUR', 'MVR', 'MWK', 'MXN', 'MYR', 'MZN', 'NAD', 'NGN', 'NIO', 'NOK',
              'NPR', 'NZD', 'OMR', 'PAB', 'PEN', 'PGK', 'PHP', 'PKR', 'PLN', 'PYG', 'QAR', 'RON', 'RSD', 'RUB', 'RWF',
              'SAR', 'SBD', 'SCR', 'SDG', 'SEK', 'SGD', 'SHP', 'SLE', 'SLL', 'SOS', 'SRD', 'SSP', 'STN', 'SYP', 'SZL',
              'THB', 'TJS', 'TMT', 'TND', 'TOP', 'TRY', 'TTD', 'TVD', 'TWD', 'TZS', 'UAH', 'UGX', 'UYU', 'UZS', 'VES',
              'VND', 'VUV', 'WST', 'XAF', 'XCD', 'XDR', 'XOF', 'XPF', 'YER', 'ZAR', 'ZMW', 'ZWL']

root = tk.Tk()
root.title('Currency calculator')

from_currency = tk.StringVar()
to_currency = tk.StringVar()
from_listbox = ttk.Combobox(root, width=5, textvariable=from_currency)
from_listbox['values'] = currencies
amount_entry = ttk.Entry(root, width=10)
to_listbox = ttk.Combobox(root, width=5, textvariable=to_currency)
to_listbox['values'] = currencies
text = ttk.Entry(root, width=50, state='readonly')

ttk.Separator().grid(row=0, columnspan=3, pady=5, sticky='WE')
ttk.Label(text='From:').grid(row=1, column=0, padx=5, sticky='W')
ttk.Label(text='Amount:').grid(row=1, column=1, padx=10)
ttk.Label(text='To:').grid(row=1, column=2)
from_listbox.grid(row=2, column=0, padx=5, sticky='W')
amount_entry.grid(row=2, column=1, padx=10)
to_listbox.grid(row=2, column=2, padx=5, sticky=tk.E)
ttk.Separator().grid(row=3, columnspan=3, pady=5, sticky='WE')
ttk.Button(
    text='Convert',
    command=lambda: convert_currency(from_currency.get(), to_currency.get(), amount_entry.get())).grid(row=4, column=1)
ttk.Separator().grid(row=5, columnspan=3, pady=5, sticky='WE')
text.grid(row=6, columnspan=3, padx=5)
ttk.Separator().grid(row=7, columnspan=3, pady=5, sticky='WE')

root.mainloop()
