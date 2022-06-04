import pprint
from python_client.openapi_client.api_client import ApiClient
from python_client.openapi_client.api_client import ApiException
from python_client.openapi_client.api.heart_rate_api import HeartRateApi


class HeartRateRepository:

    def __init__(self, configuration):
        api_client = ApiClient(configuration)
        self.api_instance = HeartRateApi(api_client)

    def save(self, measureDTO):
        try:
            api_response = self.api_instance.save_heart_rate(measureDTO)
            print(str(api_response))
        except ApiException as e:
            print("Exception when calling HeartRateApi->save_heart_rate: %s\n" % e)
