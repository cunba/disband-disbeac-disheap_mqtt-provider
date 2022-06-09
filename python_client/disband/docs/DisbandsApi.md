# openapi_client.DisbandsApi

All URIs are relative to *http://63.33.86.240:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_disband**](DisbandsApi.md#delete_disband) | **DELETE** /disbands/{id} | Delete disband
[**delete_disbands_by_user_id**](DisbandsApi.md#delete_disbands_by_user_id) | **DELETE** /disbands/users/{userId} | Delete disbands by user ID
[**get_disband_by_id**](DisbandsApi.md#get_disband_by_id) | **GET** /disbands/{id} | Get disband by ID
[**get_disband_by_mac**](DisbandsApi.md#get_disband_by_mac) | **GET** /disbands/macs/{mac} | Get disbands by mac
[**get_disbands_by_user_id**](DisbandsApi.md#get_disbands_by_user_id) | **GET** /disbands/users/{userId} | Get disbands by user ID
[**save_disband**](DisbandsApi.md#save_disband) | **POST** /disbands | Save disband
[**update_disband**](DisbandsApi.md#update_disband) | **PUT** /disbands/{id} | Update disband
[**update_disband_user_id**](DisbandsApi.md#update_disband_user_id) | **PATCH** /disbands/{id}/user/{userId} | Update user ID


# **delete_disband**
> Disband delete_disband(id)

Delete disband

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import openapi_client
from api.service import disbands_api
from openapi_client.model.disband import Disband
from openapi_client.model.error_response import ErrorResponse
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
    api_instance = disbands_api.DisbandsApi(api_client)
    id = "id_example" # str | Disband id

    # example passing only required values which don't have defaults set
    try:
        # Delete disband
        api_response = api_instance.delete_disband(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DisbandsApi->delete_disband: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Disband id |

### Return type

[**Disband**](Disband.md)

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
**404** | Disband not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_disbands_by_user_id**
> [Disband] delete_disbands_by_user_id(user_id)

Delete disbands by user ID

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import openapi_client
from api.service import disbands_api
from openapi_client.model.disband import Disband
from openapi_client.model.error_response import ErrorResponse
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
    api_instance = disbands_api.DisbandsApi(api_client)
    user_id = "userId_example" # str | User id

    # example passing only required values which don't have defaults set
    try:
        # Delete disbands by user ID
        api_response = api_instance.delete_disbands_by_user_id(user_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DisbandsApi->delete_disbands_by_user_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User id |

### Return type

[**[Disband]**](Disband.md)

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

# **get_disband_by_id**
> Disband get_disband_by_id(id)

Get disband by ID

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import openapi_client
from api.service import disbands_api
from openapi_client.model.disband import Disband
from openapi_client.model.error_response import ErrorResponse
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
    api_instance = disbands_api.DisbandsApi(api_client)
    id = "id_example" # str | Disband ID

    # example passing only required values which don't have defaults set
    try:
        # Get disband by ID
        api_response = api_instance.get_disband_by_id(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DisbandsApi->get_disband_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Disband ID |

### Return type

[**Disband**](Disband.md)

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
**404** | Disband not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_disband_by_mac**
> Disband get_disband_by_mac(mac)

Get disbands by mac

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import openapi_client
from api.service import disbands_api
from openapi_client.model.disband import Disband
from openapi_client.model.error_response import ErrorResponse
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
    api_instance = disbands_api.DisbandsApi(api_client)
    mac = "mac_example" # str | Mac

    # example passing only required values which don't have defaults set
    try:
        # Get disbands by mac
        api_response = api_instance.get_disband_by_mac(mac)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DisbandsApi->get_disband_by_mac: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mac** | **str**| Mac |

### Return type

[**Disband**](Disband.md)

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

# **get_disbands_by_user_id**
> [Disband] get_disbands_by_user_id(user_id)

Get disbands by user ID

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import openapi_client
from api.service import disbands_api
from openapi_client.model.disband import Disband
from openapi_client.model.error_response import ErrorResponse
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
    api_instance = disbands_api.DisbandsApi(api_client)
    user_id = "userId_example" # str | User ID

    # example passing only required values which don't have defaults set
    try:
        # Get disbands by user ID
        api_response = api_instance.get_disbands_by_user_id(user_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DisbandsApi->get_disbands_by_user_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User ID |

### Return type

[**[Disband]**](Disband.md)

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

# **save_disband**
> Disband save_disband(disband_dto)

Save disband

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import openapi_client
from api.service import disbands_api
from openapi_client.model.disband import Disband
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.disband_dto import DisbandDTO
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
    api_instance = disbands_api.DisbandsApi(api_client)
    disband_dto = DisbandDTO(
        mac="mac_example",
        model="model_example",
        version="version_example",
        date=1,
        user_id="user_id_example",
    ) # DisbandDTO | 

    # example passing only required values which don't have defaults set
    try:
        # Save disband
        api_response = api_instance.save_disband(disband_dto)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DisbandsApi->save_disband: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **disband_dto** | [**DisbandDTO**](DisbandDTO.md)|  |

### Return type

[**Disband**](Disband.md)

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
**401** | Unauthorize |  -  |
**404** | User not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_disband**
> HandledResponse update_disband(id, disband_dto)

Update disband

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import openapi_client
from api.service import disbands_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.disband_dto import DisbandDTO
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
    api_instance = disbands_api.DisbandsApi(api_client)
    id = "id_example" # str | Disband id
    disband_dto = DisbandDTO(
        mac="mac_example",
        model="model_example",
        version="version_example",
        date=1,
        user_id="user_id_example",
    ) # DisbandDTO | 

    # example passing only required values which don't have defaults set
    try:
        # Update disband
        api_response = api_instance.update_disband(id, disband_dto)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DisbandsApi->update_disband: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Disband id |
 **disband_dto** | [**DisbandDTO**](DisbandDTO.md)|  |

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
**401** | Unauthorized |  -  |
**404** | Disband not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_disband_user_id**
> HandledResponse update_disband_user_id(id, user_id)

Update user ID

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import openapi_client
from api.service import disbands_api
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
    api_instance = disbands_api.DisbandsApi(api_client)
    id = "id_example" # str | Disband ID
    user_id = "userId_example" # str | New user ID

    # example passing only required values which don't have defaults set
    try:
        # Update user ID
        api_response = api_instance.update_disband_user_id(id, user_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DisbandsApi->update_disband_user_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Disband ID |
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
**404** | Disband not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

