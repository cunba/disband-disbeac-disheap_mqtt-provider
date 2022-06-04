import pprint
from python_client import ApiClient
from python_client import ApiException
from python_client import AmbientNoisesApi


class AmbientNoiseRepository:

    def __init__(self, configuration):
        api_client = ApiClient(configuration)
        self.api_instance = AmbientNoisesApi(api_client)

    def save(self, measureDTO):
        try:
            api_response = self.api_instance.save_ambient_noise(measureDTO)
            print(str(api_response))
        except ApiException as e:
            print("Exception when calling AmbientNoisesApi->save_ambient_noise: %s\n" % e)
