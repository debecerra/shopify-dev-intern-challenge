import requests
from decouple import config


class OpenWeatherAPI:
    """ Controller for interacting with the Open Weather API.
    """

    base = 'https://api.openweathermap.org/data/2.5/weather'
    params = {
        'appid': config('OPENWEATHER_API_KEY'),  # defined in .env
        'units': 'metric'
    }

    def get_weather(self, city, country):
        """ Gets the temperature and weather of a city.

        @param city: The city to check the weather for
        @param country: The country in which the city resides

        @returns (temp, weather) where temp is the current temperature in the city in Celsius and weather is a 
            brief description of the weather in the city
        """

        params = {
            'q': f'{city},{country}',
            **self.params,
        }
        response = requests.get(self.base, params=params)

        if response.status_code == 200:
            temp = response.json()['main']['temp']
            weather = response.json()['weather'][0]['description']
        else:
            temp = None
            weather = 'no weather info'

        return temp, weather
