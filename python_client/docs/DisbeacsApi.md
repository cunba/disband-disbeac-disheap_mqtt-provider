# openapi_client.DisbeacsApi

All URIs are relative to *http://63.33.86.240:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_disbeac**](DisbeacsApi.md#delete_disbeac) | **DELETE** /disbeacs/{id} | Delete disbeac
[**delete_disbeacs_by_user_id**](DisbeacsApi.md#delete_disbeacs_by_user_id) | **DELETE** /disbeacs/users/{userId} | Delete disbeacs by user ID
[**get_by_id6**](DisbeacsApi.md#get_by_id6) | **GET** /disbeacs/{id} | Get disbeac by ID
[**get_disbeacs_by_mac**](DisbeacsApi.md#get_disbeacs_by_mac) | **GET** /disbeacs/macs/{mac} | Get disbeac by mac
[**get_disbeacs_by_user_id**](DisbeacsApi.md#get_disbeacs_by_user_id) | **GET** /disbeacs/users/{userId} | Get disbeacs by user ID
[**savedisbeac**](DisbeacsApi.md#savedisbeac) | **POST** /disbeacs | Save disbeac
[**update_disbeac**](DisbeacsApi.md#update_disbeac) | **PUT** /disbeacs/{id} | Update disbeac
[**update_user_id**](DisbeacsApi.md#update_user_id) | **PATCH** /disbeacs/{id}/user/{userId} | Update user ID


# **delete_disbeac**
> Disbeac delete_disbeac(id)

Delete disbeac

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import openapi_client
from api.service import disbeacs_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.disbeac import Disbeac
from pprint import pprint
# Defining the host is optional and defaults to http://63.33.86.240:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://63.33.86.240:8080"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearer
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = disbeacs_api.DisbeacsApi(api_client)
    id = "id_example" # str | Disbeac id

    # example passing only required values which don't have defaults set
    try:
        # Delete disbeac
        api_response = api_instance.delete_disbeac(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DisbeacsApi->delete_disbeac: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Disbeac id |

### Return type

[**Disbeac**](Disbeac.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**404** | Disbeac not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_disbeacs_by_user_id**
> [Disbeac] delete_disbeacs_by_user_id(user_id)

Delete disbeacs by user ID

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import openapi_client
from api.service import disbeacs_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.disbeac import Disbeac
from pprint import pprint
# Defining the host is optional and defaults to http://63.33.86.240:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://63.33.86.240:8080"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearer
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = disbeacs_api.DisbeacsApi(api_client)
    user_id = "userId_example" # str | User id

    # example passing only required values which don't have defaults set
    try:
        # Delete disbeacs by user ID
        api_response = api_instance.delete_disbeacs_by_user_id(user_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DisbeacsApi->delete_disbeacs_by_user_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User id |

### Return type

[**[Disbeac]**](Disbeac.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_by_id6**
> Disbeac get_by_id6(id)

Get disbeac by ID

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import openapi_client
from api.service import disbeacs_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.disbeac import Disbeac
from pprint import pprint
# Defining the host is optional and defaults to http://63.33.86.240:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://63.33.86.240:8080"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearer
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = disbeacs_api.DisbeacsApi(api_client)
    id = "id_example" # str | Disbeac ID

    # example passing only required values which don't have defaults set
    try:
        # Get disbeac by ID
        api_response = api_instance.get_by_id6(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DisbeacsApi->get_by_id6: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Disbeac ID |

### Return type

[**Disbeac**](Disbeac.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**404** | Disbeac not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_disbeacs_by_mac**
> [Disbeac] get_disbeacs_by_mac(mac)

Get disbeac by mac

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import openapi_client
from api.service import disbeacs_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.disbeac import Disbeac
from pprint import pprint
# Defining the host is optional and defaults to http://63.33.86.240:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://63.33.86.240:8080"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearer
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = disbeacs_api.DisbeacsApi(api_client)
    mac = "mac_example" # str | Mac

    # example passing only required values which don't have defaults set
    try:
        # Get disbeac by mac
        api_response = api_instance.get_disbeacs_by_mac(mac)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DisbeacsApi->get_disbeacs_by_mac: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mac** | **str**| Mac |

### Return type

[**[Disbeac]**](Disbeac.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_disbeacs_by_user_id**
> [Disbeac] get_disbeacs_by_user_id(user_id)

Get disbeacs by user ID

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import openapi_client
from api.service import disbeacs_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.disbeac import Disbeac
from pprint import pprint
# Defining the host is optional and defaults to http://63.33.86.240:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://63.33.86.240:8080"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearer
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = disbeacs_api.DisbeacsApi(api_client)
    user_id = "userId_example" # str | User ID

    # example passing only required values which don't have defaults set
    try:
        # Get disbeacs by user ID
        api_response = api_instance.get_disbeacs_by_user_id(user_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DisbeacsApi->get_disbeacs_by_user_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User ID |

### Return type

[**[Disbeac]**](Disbeac.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **savedisbeac**
> Disbeac savedisbeac(disbeac_dto)

Save disbeac

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import openapi_client
from api.service import disbeacs_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.disbeac import Disbeac
from openapi_client.model.disbeac_dto import DisbeacDTO
from pprint import pprint
# Defining the host is optional and defaults to http://63.33.86.240:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://63.33.86.240:8080"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearer
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = disbeacs_api.DisbeacsApi(api_client)
    disbeac_dto = DisbeacDTO(
        mac="mac_example",
        model="model_example",
        version="version_example",
        user_id="user_id_example",
    ) # DisbeacDTO | 

    # example passing only required values which don't have defaults set
    try:
        # Save disbeac
        api_response = api_instance.savedisbeac(disbeac_dto)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DisbeacsApi->savedisbeac: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **disbeac_dto** | [**DisbeacDTO**](DisbeacDTO.md)|  |

### Return type

[**Disbeac**](Disbeac.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**201** | CREATED |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | User not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_disbeac**
> HandledResponse update_disbeac(id, disbeac_dto)

Update disbeac

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import openapi_client
from api.service import disbeacs_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.handled_response import HandledResponse
from openapi_client.model.disbeac_dto import DisbeacDTO
from pprint import pprint
# Defining the host is optional and defaults to http://63.33.86.240:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://63.33.86.240:8080"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearer
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = disbeacs_api.DisbeacsApi(api_client)
    id = "id_example" # str | Disbeac id
    disbeac_dto = DisbeacDTO(
        mac="mac_example",
        model="model_example",
        version="version_example",
        user_id="user_id_example",
    ) # DisbeacDTO | 

    # example passing only required values which don't have defaults set
    try:
        # Update disbeac
        api_response = api_instance.update_disbeac(id, disbeac_dto)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DisbeacsApi->update_disbeac: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Disbeac id |
 **disbeac_dto** | [**DisbeacDTO**](DisbeacDTO.md)|  |

### Return type

[**HandledResponse**](HandledResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | Disbeac not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_id**
> HandledResponse update_user_id(id, user_id)

Update user ID

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import openapi_client
from api.service import disbeacs_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.handled_response import HandledResponse
from pprint import pprint
# Defining the host is optional and defaults to http://63.33.86.240:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://63.33.86.240:8080"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearer
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = disbeacs_api.DisbeacsApi(api_client)
    id = "id_example" # str | Disbeac ID
    user_id = "userId_example" # str | New user ID

    # example passing only required values which don't have defaults set
    try:
        # Update user ID
        api_response = api_instance.update_user_id(id, user_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DisbeacsApi->update_user_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Disbeac ID |
 **user_id** | **str**| New user ID |

### Return type

[**HandledResponse**](HandledResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**404** | Disbeac not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

