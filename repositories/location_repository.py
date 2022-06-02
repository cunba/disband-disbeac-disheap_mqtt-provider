import pprint
from python_client.openapi_client.api_client import ApiClient
from python_client.openapi_client.api_client import ApiException
from python_client.openapi_client.api.locations_disbeacs_api import LocationsDisbeacsApi


class LocationRepository:

    def __init__(self, configuration):
        api_client = ApiClient(configuration)
        self.api_instance = LocationsDisbeacsApi(api_client)

    def save(self, locationDTO):
        try:
            api_response = self.api_instance.save_location(locationDTO)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling LocationsDisbeacsApi->save_Location: %s\n" % e)
