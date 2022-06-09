import pprint
from python_client.disband.openapi_client.api_client import ApiClient
from python_client.disband.openapi_client.api_client import ApiException
from python_client.disband.openapi_client.api.service.humidity_api import HumidityApi


class HumidityRepository:

    def __init__(self, configuration):
        api_client = ApiClient(configuration)
        self.api_instance = HumidityApi(api_client)

    def save(self, measureDTO):
        try:
            api_response = self.api_instance.save_humidity(measureDTO)
            print(str(api_response))
            print()
        except ApiException as e:
            print("Exception when calling HumidityApi->save_humidity: %s\n" % e)
