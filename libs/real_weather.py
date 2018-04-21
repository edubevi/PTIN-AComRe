import forecastio

api_key = "413580f0df4f6db0481a5611321ac32a"
lat = 41.222576
lng = 1.732158

class DummyWeather:
    def __init__(self):
        self.temperature = 16
        self.humidity = 0.68
        self.pressure = 1013

def get_current_data():
    try:
        forecast = forecastio.load_forecast(api_key, lat, lng, units='si')
        current = forecast.currently()
        return current
    except:
        mock_conditions = DummyWeather()
        return mock_conditions
