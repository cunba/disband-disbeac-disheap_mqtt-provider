from python_client.disheap.openapi_client.api_client import ApiClient
from python_client.disheap.openapi_client.api_client import ApiException
from python_client.disheap.openapi_client.api.service.login_api import LoginApi
from python_client.disheap.openapi_client.model.jwt_request import JwtRequest


class LoginRepository:

    def __init__(self, configuration):
        api_client = ApiClient(configuration)
        self.api_instance = LoginApi(api_client)

    def login(self, email, password):
        jwt_request = JwtRequest(
            email=email,
            password=password
        )
        try:
            api_response = self.api_instance.login(jwt_request)
            token = api_response.get('token')
            return token
        except ApiException as e:
            print("Exception when calling LoginApi->login: %s\n" % e)
