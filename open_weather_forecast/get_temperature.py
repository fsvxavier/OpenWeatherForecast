import json
import requests
from functools import wraps, reduce
from requests.exceptions import RequestException
import time

URL = 'http://api.openweathermap.org/data/2.5/weather?q=London,uk'
FORECAST_URL = 'http://api.openweathermap.org/data/2.5/forecast/city?q=London,uk'


def get_from_dict(data_dict, list_of_keys):
    return reduce(lambda d, k: d[k], list_of_keys, data_dict)


def auto_tries(exception_to_catch, tries=4, delay=3, logger=None):
    """
    Decorator to auto_tries the weather info

    :param tries:
    :param delay: Expressed in seconds, the waiting time between tries
    :param logger:
    :return:
    """
    def deco_retry(f):
        @wraps(f)
        def f_retry(*args, **kwargs):
            internal_tries = tries
            last_value = None
            while internal_tries > 0:
                try:
                    last_value = f(*args, **kwargs)
                except exception_to_catch:
                    time.sleep(delay)
                internal_tries -= 1
            return last_value

        return f_retry

    return deco_retry


@auto_tries(RequestException, tries=4, delay=1)
def http_retrieve(url):
    r = requests.get(url)
    if r.ok:
        return r.json()
    else:
        return {}


def get_temperature(url, given_keys):
    today_temperature = http_retrieve(url)
    if not today_temperature:
        return False, today_temperature
    else:
        main_temperature = today_temperature.get("main")
        for key in given_keys:
            today_temperature[key] = today_temperature.get(key)


def get_temperatures(url, given_keys):
    r = requests.get(url)
    dictionary = {}
    if r.ok:
        body_res = json.loads(r.text).get('list')
        for day in body_res:
            datetime = day.get('dt_txt')
            dictionary[datetime] = {}
            for key in given_keys:
                dictionary[datetime][key] = day.get(key)
        return True, dictionary
    else:
        return False, dictionary
