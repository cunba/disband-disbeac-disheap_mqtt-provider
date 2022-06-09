import pprint
from python_client.disband.openapi_client.api_client import ApiClient
from python_client.disband.openapi_client.api_client import ApiException
from python_client.disband.openapi_client.api.service.disbands_api import DisbandsApi


class DisbandRepository:

    def __init__(self, configuration):
        api_client = ApiClient(configuration)
        self.api_instance = DisbandsApi(api_client)

    def save(self, disbandDTO):
        try:
            api_response = self.api_instance.save_disband(disbandDTO)
            print(str(api_response))
            print()
        except ApiException as e:
            print("Exception when calling DisbandApi->save_disband: %s\n" % e)
