import unittest


class SimpleWidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.url = 'http://api.openweathermap.org/data/2.5/forecast/city?q=London,uk'

    def tearDown(self):
        pass
