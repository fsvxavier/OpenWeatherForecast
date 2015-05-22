import requests
from functools import wraps, reduce
from requests.exceptions import RequestException
import time

URL = 'http://api.openweathermap.org/data/2.5/weather?q=London,uk'
FORECAST_URL = 'http://api.openweathermap.org/data/2.5/forecast/city?q=London,uk'


def get_from_dict(data_dict, list_of_keys):
    list_of_keys = [list_of_keys] if not isinstance(list_of_keys, list) else list_of_keys
    return reduce(lambda d, k: d.get(k, {}), list_of_keys, data_dict)


def set_a_dict(data_dict, list_of_keys, value):
    get_from_dict(data_dict, list_of_keys[:-1])[list_of_keys[-1]] = value


def auto_tries(exception_to_catch, tries=4, delay=3):
    """
    Decorator to auto_tries the weather info

    :param tries:
    :param delay: Expressed in seconds, the waiting time between tries
    :return:
    """

    def deco_retry(f):
        @wraps(f)
        def f_retry(*args, **kwargs):
            for internal_tries in range(tries):
                try:
                    return f(*args, **kwargs)
                except exception_to_catch:
                    time.sleep(delay)
            return None

        return f_retry

    return deco_retry


@auto_tries(RequestException, tries=4, delay=1)
def http_retrieve(url):
    r = requests.get(url)
    if r.ok:
        return r.json()
    else:
        return {}


def create_dictionary(temperatures_history, information_schema, dictionary=None):
    if not dictionary:
        dictionary = dict()

    for key in information_schema:
        if isinstance(temperatures_history, dict):
            value = temperatures_history.get(key, {})
        else:
            import ipdb
            ipdb.set_trace()
            for element, sub_info in zip(temperatures_history, information_schema.get(key)):
                create_dictionary(element, sub_info, dictionary)
            return dictionary

        if not isinstance(information_schema.get(key), type(value)):
            msg = "Types from information schema and the information retrieved does not match"
            raise ValueError(msg)

        if isinstance(value, (list, dict)):
            dictionary[key] = type(value)()
            return create_dictionary(temperatures_history.get(key), information_schema, dictionary)
        else:
            if isinstance(dictionary[key], list):
                dictionary[key].append(value)
            else:
                dictionary[key] = value
        return dictionary


def get_temperature(url, information_schema):
    temperatures_history = http_retrieve(url)
    if not temperatures_history:
        return False, {}
    else:
        try:
            return True, create_dictionary(temperatures_history, information_schema)
        except (ValueError, KeyError):
            return False, {}
