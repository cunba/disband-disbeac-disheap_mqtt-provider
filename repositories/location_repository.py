import pprint
from python_client.disbeac.openapi_client.api_client import ApiClient
from python_client.disbeac.openapi_client.api_client import ApiException
from python_client.disbeac.openapi_client.api.service.locations_api import LocationsApi


class LocationRepository:

    def __init__(self, configuration):
        api_client = ApiClient(configuration)
        self.api_instance = LocationsApi(api_client)

    def save(self, locationDTO):
        try:
            api_response = self.api_instance.save_location(locationDTO)
            print(str(api_response))
        except ApiException as e:
            print("Exception when calling LocationsDisbeacsApi->save_Location: %s\n" % e)
