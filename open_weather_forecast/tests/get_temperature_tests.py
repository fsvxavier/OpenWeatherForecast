import unittest
from open_weather_forecast.get_temperature import get_temperature


class GetTemperatureTest(unittest.TestCase):
    def setUp(self):
        self.url = 'http://api.openweathermap.org/data/2.5/forecast/city?q={}'.format("London,uk")

    def tearDown(self):
        pass

    def basic_test(self):
        information_schema = {
            "list": [
                {"main": [{"temp": int,
                           "temp_min": int,
                           "temp_max": int}
                          ],
                 "dt_txt": str
                 },
                ]
        }
        print(get_temperature(self.url, information_schema))