import forecastio

api_key = "e326fd210528c506641f454726a95bfc"
lat = 41.222576
lng = 1.732158


def get_current_data():
    forecast = forecastio.load_forecast(api_key, lat, lng, units='si')
    current = forecast.currently()
    return current
