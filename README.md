# Weather forecast

[![Build Status](https://travis-ci.org/enanablancaynumeros/OpenWeatherForecast.svg?branch=master)](https://travis-ci.org/enanablancaynumeros/OpenWeatherForecast)
[![Coverage Status](https://coveralls.io/repos/enanablancaynumeros/OpenWeatherForecast/badge.svg)](https://coveralls.io/r/enanablancaynumeros/OpenWeatherForecast)
[![Latest Version](https://pypip.in/version/OpenWeatherForecast/badge.svg)](https://pypi.python.org/pypi/OpenWeatherForecast/)
[![Supported Python versions](https://pypip.in/py_versions/OpenWeatherForecast/badge.svg)](https://pypi.python.org/pypi/OpenWeatherForecast/)
[![Supported Python implementations](https://pypip.in/implementation/OpenWeatherForecast/badge.svg)](https://pypi.python.org/pypi/OpenWeatherForecast/)
[![Development Status](https://pypip.in/status/OpenWeatherForecast/badge.svg)](https://pypi.python.org/pypi/OpenWeatherForecast/)
[![Wheel Status](https://pypip.in/wheel/OpenWeatherForecast/badge.svg)](https://pypi.python.org/pypi/OpenWeatherForecast/)

Openweather python wrapper to forecast weather data.

OpenWeatherForecast is released under the [MIT license](https://github.com/enanablancaynumeros/weather_forecast/blob/master/LICENSE.txt). The source code is on [GitHub](https://github.com/enanablancaynumeros) and [issues are also tracked on GitHub](https://github.com/enanablancaynumeros/weather_forecast/issues).

### Install 
#### Pypi
```bash
pip install openweatherforecast
```

#### Manual
```bash
git clone git@github.com:enanablancaynumeros/OpenWeatherForecast.git
cd OpenWeatherForecast
python setup.py install
# Make sure it works
python setup.py test
```

#### Db configuration
Change the folder in constants or use the one defined in "/etc/openweather/settings.yaml"
```bash
sudo mkdir /etc/openweather/
sudo chmod 777 -R /etc/openweather/
cp contrib/settings.yaml /etc/openweather/
```

### Code example

```python
from open_weather_forecast.get_temperature import GetTemperature
from open_weather_forecast.constants import WEATHER_INFORMATION_SCHEMA

url = 'http://api.openweathermap.org/data/2.5/forecast/city?q={}'.format("London,uk")
get_temp_manager = GetTemperature()
info = get_temp_manager.http_retrieve(url=url)
info_filtered_by_schema = get_temp_manager.filter_information(info, WEATHER_INFORMATION_SCHEMA)
```

### Run test
```shell
python setup.py test

or 

nosetest openweatherforecast

```


See [Pypi](https://pypi.python.org/pypi/openweatherforecast/0.1.0) project page.



[![Bitdeli Badge](https://d2weczhvl823v0.cloudfront.net/enanablancaynumeros/openweatherforecast/trend.png)](https://bitdeli.com/free "Bitdeli Badge")

