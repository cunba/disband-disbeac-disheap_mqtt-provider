import pprint
from python_client.openapi_client.api_client import ApiClient
from python_client.openapi_client.api_client import ApiException
from python_client.openapi_client.api.disbeacs_api import DisbeacsApi


class DisbeacRepository:

    def __init__(self, configuration):
        api_client = ApiClient(configuration)
        self.api_instance = DisbeacsApi(api_client)

    def save(self, disbeacDTO):
        try:
            api_response = self.api_instance.savedisbeac(disbeacDTO)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling DisbeacApi->save_disbeac: %s\n" % e)
