'''
This web service extends the Alphavantage api by creating a visualization module, 
converting json query results retuned from the api into charts and other graphics. 

This is where you should add your code to function query the api
'''

import pygal
import requests
from flask import flash
from datetime import timedelta
from .helpers import *

CHART_TYPES = ['Bar', 'Line']
TIME_SERIES = {
    'Intraday': {'key': 'Time Series (60min)', 'scale': {'hours': 1}},
    'Daily': {'key': 'Time Series (Daily)', 'scale': {'days': 1}},
    'Weekly': {'key': 'Weekly Time Series', 'scale': {'days': 1}},
    'Monthly': {'key': 'Monthly Time Series', 'scale': {'days': 1}}
}


class StockDataChart:

    __apiKey = 'AU4UXQO6WFYENR4J'
    default_opts = {'x_label_rotation': 45}
    url = 'https://www.alphavantage.co/query?'
    data = {}

    def __init__(self, symbol, time_series, start_date, end_date):
        self.symbol = symbol
        self.time_series = time_series
        self.start_date = start_date
        self.end_date = end_date
        self.default_opts['title'] = f'{self.symbol} stocks for {date_to_str(self.start_date)} - {date_to_str(self.end_date)}'
        self.url += f'function=TIME_SERIES_{time_series.upper()}&symbol={symbol}&interval=60min&apikey={self.__apiKey}'
        self.fetch_data()

    def fetch_data(self):
        self.data = requests.get(self.url).json()

    def render(self, chart_type, opts={}):
        opts = {**self.default_opts, **opts}
        if chart_type == 'Bar':
            chart = pygal.Bar(**opts)
        elif chart_type == 'Line':
            chart = pygal.Line(**opts)
        else:
            return None
        return self.build(chart).render_data_uri()

    def build(self, chart):
        x_labels = []
        points = {'OPEN': [], 'HIGH': [], 'LOW': [], 'CLOSE': []}
        try:
            stock_data = self.data[TIME_SERIES[self.time_series]['key']]
        except KeyError:
            flash('Something went wrong while getting the stock data.')
            return chart
        dt = self.start_date
        while dt <= self.end_date:
            date_format = DF_INTRADAY if self.time_series == 'Intraday' else DF_DEFAULT
            date_str = date_to_str(dt, date_format)
            try:
                points['OPEN'].append(float(stock_data[date_str]['1. open']))
                points['HIGH'].append(float(stock_data[date_str]['2. high']))
                points['LOW'].append(float(stock_data[date_str]['3. low']))
                points['CLOSE'].append(float(stock_data[date_str]['4. close']))
            except KeyError:
                continue
            else:
                x_labels.append(date_str)
            finally:
                dt += timedelta(**TIME_SERIES[self.time_series]['scale'])
        chart.x_labels = x_labels
        for line in points:
            chart.add(line, points[line])
        return chart
