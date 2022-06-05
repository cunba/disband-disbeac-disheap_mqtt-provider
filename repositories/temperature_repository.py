import pprint
from python_client.openapi_client.api_client import ApiClient
from python_client.openapi_client.api_client import ApiException
from python_client.openapi_client.api.temperatures_api import TemperaturesApi


class TemperatureRepository:

    def __init__(self, configuration):
        api_client = ApiClient(configuration)
        self.api_instance = TemperaturesApi(api_client)

    def save(self, measureDTO):
        try:
            api_response = self.api_instance.save_temperature(measureDTO)
            print(str(api_response))
            print()
        except ApiException as e:
            print("Exception when calling TemperatureApi->save_temperature: %s\n" % e)
