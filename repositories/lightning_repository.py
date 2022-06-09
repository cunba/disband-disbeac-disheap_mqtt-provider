import pprint
from python_client.disband.openapi_client.api_client import ApiClient
from python_client.disband.openapi_client.api_client import ApiException
from python_client.disband.openapi_client.api.service.lightnings_api import LightningsApi


class LightningRepository:

    def __init__(self, configuration):
        api_client = ApiClient(configuration)
        self.api_instance = LightningsApi(api_client)

    def save(self, lightningDTO):
        try:
            api_response = self.api_instance.save_lightning(lightningDTO)
            print(str(api_response))
            print()
        except ApiException as e:
            print("Exception when calling LightningApi->save_lightning: %s\n" % e)
