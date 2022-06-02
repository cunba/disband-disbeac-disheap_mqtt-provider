# openapi_client.LoginApi

All URIs are relative to *http://63.33.86.240:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**login**](LoginApi.md#login) | **POST** /login | Login


# **login**
> JwtResponse login(jwt_request)

Login

### Example


```python
import time
import openapi_client
from api.service import login_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.jwt_request import JwtRequest
from openapi_client.model.jwt_response import JwtResponse
from pprint import pprint
# Defining the host is optional and defaults to http://63.33.86.240:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://63.33.86.240:8080"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = login_api.LoginApi(api_client)
    jwt_request = JwtRequest(
        email="email_example",
        password="password_example",
    ) # JwtRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Login
        api_response = api_instance.login(jwt_request)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling LoginApi->login: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jwt_request** | [**JwtRequest**](JwtRequest.md)|  |

### Return type

[**JwtResponse**](JwtResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

