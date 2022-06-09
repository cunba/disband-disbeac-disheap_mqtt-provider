import pprint
from python_client.disband.openapi_client.api_client import ApiClient
from python_client.disband.openapi_client.api_client import ApiException
from python_client.disband.openapi_client.api.service.pressure_api import PressureApi


class PressureRepository:

    def __init__(self, configuration):
        api_client = ApiClient(configuration)
        self.api_instance = PressureApi(api_client)

    def save(self, measureDTO):
        try:
            api_response = self.api_instance.save_pressure(measureDTO)
            print(str(api_response))
            print()
        except ApiException as e:
            print("Exception when calling PressureApi->save_pressure: %s\n" % e)
