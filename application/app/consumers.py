import json
import random

from channels.generic.websocket import WebsocketConsumer
from .models import *


class WSConsumerNews(WebsocketConsumer):
    def connect(self):
        print("function connect")
        self.accept()
        self.send(json.dumps({'status': 'connected'}))

    def send_news(self):
        print("function send_news")
        result_dict = {
            'status': 'data_news',
            'values': []}
        for news in News.objects.all():
            result_dict['values'].append({
                'name': news.name,
                'date': str(news.date),
                'short_text': news.short_text,
                'text': news.text,
                'category': str(news.category),
                'source': str(news.source)
            })

        self.send(json.dumps(result_dict))

    # Когда приходит сообщение с клиента
    def receive(self, text_data=None, bytes_data=None):
        if text_data == 'send_news':
            self.send_news()
            print("Новости отправлены")
        else:
            print("Garbage")


    def disconnect(self, code):
        print("function disconnect")


LENGTH_DATA = 6
DATES = ['23.04 7:00', '23.04 10:00', '23.04 13:00', '23.04 16:00', '23.04 19:00', '23.04 22:00']


def get_rates(currency1, currency2, date):
    if currency1 == 'USD':
        number = 75.0 + (random.randint(1, 10) / 10)
        return number
    elif currency1 == 'EUR':
        number = 80.0 + (random.randint(1, 20) / 10)
        return number
    else:
        return 60.0 + (random.randint(1, 50) / 10)


class WSConsumerRates(WebsocketConsumer):
    def get_day_data(self, currency1, currency2):
        x_data = DATES
        y_data = []
        for i in range(LENGTH_DATA):
            y_data.append(get_rates(currency1, currency2, ''))
        return json.dumps({
            'currency1': currency1,
            'currency2': currency2,
            'status': 'day',
            'x': x_data,
            'y': y_data,
            'value': 75.0 + (random.randint(1, 10) / 10)
        })

    def get_hour_data(self, currency1, currency2):
        x_data = DATES
        y_data = []
        for i in range(LENGTH_DATA):
            y_data.append(get_rates(currency1, currency2, ''))
        return json.dumps({
            'currency1': currency1,
            'currency2': currency2,
            'status': 'hour',
            'x': x_data,
            'y': y_data
        })

    def get_halfhour_data(self, currency1, currency2):
        x_data = DATES
        y_data = []
        for i in range(LENGTH_DATA):
            y_data.append(get_rates(currency1, currency2, ''))
        return json.dumps({
            'currency1': currency1,
            'currency2': currency2,
            'status': 'halfhour',
            'x': x_data,
            'y': y_data
        })

    def get_10min_data(self, currency1, currency2):
        x_data = DATES
        y_data = []
        for i in range(LENGTH_DATA):
            y_data.append(get_rates(currency1, currency2, ''))
        return json.dumps({
            'currency1': currency1,
            'currency2': currency2,
            'status': '10min',
            'x': x_data,
            'y': y_data
        })

    def connect(self):
        print("function connect")
        self.accept()
        self.send(json.dumps({'status': 'connected'}))

    # Когда приходит сообщение с клиента
    def receive(self, text_data=None, bytes_data=None):
        data = text_data.split('|')
        print(data)
        if len(data) == 3:
            timeseries = data[2]
        else:
            timeseries = 'day'
        currency1 = data[0]
        currency2 = data[1]
        if timeseries == 'day':
            self.send(self.get_day_data(currency1, currency2))
        elif timeseries == 'hour':
            self.send(self.get_hour_data(currency1, currency2))
        elif timeseries == 'halfhour':
            self.send(self.get_halfhour_data(currency1, currency2))
        elif timeseries == '10min':
            self.send(self.get_10min_data(currency1, currency2))
        else:
            print("Garbage")


    def disconnect(self, code):
        print("function disconnect")