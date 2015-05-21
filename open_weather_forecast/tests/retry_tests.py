import unittest
from open_weather_forecast.get_temperature import retry


class RetryDecoratorTest(unittest.TestCase):
    def setUp(self):
        self.url = 'http://api.openweathermap.org/data/2.5/forecast/city?q={}'.format("London,uk")

    def tearDown(self):
        pass

    def zero_retries_test(self):
        @retry(ValueError, tries=0, delay=0)
        def test_func():
            raise ValueError()

        assert test_func() is None

    def zero_retries_no_exception_test(self):
        @retry(ValueError, tries=0, delay=0)
        def test_func():
            return 1

        assert test_func() is None
