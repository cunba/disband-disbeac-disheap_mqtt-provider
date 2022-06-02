import pprint
from python_client.openapi_client.api_client import ApiClient
from python_client.openapi_client.api_client import ApiException
from python_client.openapi_client.api.oxygen_api import OxygenApi


class OxygenRepository:

    def __init__(self, configuration):
        api_client = ApiClient(configuration)
        self.api_instance = OxygenApi(api_client)

    def save(self, measureDTO):
        try:
            api_response = self.api_instance.save_oxygen(measureDTO)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling OxygenApi->save_oxygen: %s\n" % e)
