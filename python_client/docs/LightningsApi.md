# openapi_client.LightningsApi

All URIs are relative to *http://63.33.86.240:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_lightnings_by_disband_id**](LightningsApi.md#delete_lightnings_by_disband_id) | **DELETE** /lightnings/disbands/{disbandId} | Delete lightnings by disband ID
[**get_all_lightning**](LightningsApi.md#get_all_lightning) | **GET** /lightnings | Get all lightnings
[**get_by_id3**](LightningsApi.md#get_by_id3) | **GET** /lightnings/{id} | Get lightnint by ID
[**get_lightnings_by_date_between**](LightningsApi.md#get_lightnings_by_date_between) | **GET** /lightnings/date/between | Get lightnings by date between
[**get_lightnings_by_date_between_and_disband_id**](LightningsApi.md#get_lightnings_by_date_between_and_disband_id) | **GET** /lightnings/date/between/disband/{disbandId} | Get lightnings by date between and disband ID
[**get_lightnings_by_disband_id**](LightningsApi.md#get_lightnings_by_disband_id) | **GET** /lightnings/disbands/{disbandId} | Get lightnings by disband ID
[**save_lightning**](LightningsApi.md#save_lightning) | **POST** /lightnings | Save lightnint


# **delete_lightnings_by_disband_id**
> [Lightning] delete_lightnings_by_disband_id(disband_id)

Delete lightnings by disband ID

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import openapi_client
from api.service import lightnings_api
from openapi_client.model.lightning import Lightning
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
    api_instance = lightnings_api.LightningsApi(api_client)
    disband_id = "disbandId_example" # str | Disband id

    # example passing only required values which don't have defaults set
    try:
        # Delete lightnings by disband ID
        api_response = api_instance.delete_lightnings_by_disband_id(disband_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling LightningsApi->delete_lightnings_by_disband_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **disband_id** | **str**| Disband id |

### Return type

[**[Lightning]**](Lightning.md)

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
**404** | Not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_lightning**
> [Lightning] get_all_lightning()

Get all lightnings

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import openapi_client
from api.service import lightnings_api
from openapi_client.model.lightning import Lightning
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
    api_instance = lightnings_api.LightningsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get all lightnings
        api_response = api_instance.get_all_lightning()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling LightningsApi->get_all_lightning: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[Lightning]**](Lightning.md)

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

# **get_by_id3**
> Lightning get_by_id3(id)

Get lightnint by ID

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import openapi_client
from api.service import lightnings_api
from openapi_client.model.lightning import Lightning
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
    api_instance = lightnings_api.LightningsApi(api_client)
    id = "id_example" # str | Lightnint ID

    # example passing only required values which don't have defaults set
    try:
        # Get lightnint by ID
        api_response = api_instance.get_by_id3(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling LightningsApi->get_by_id3: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Lightnint ID |

### Return type

[**Lightning**](Lightning.md)

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
**404** | Not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_lightnings_by_date_between**
> [Lightning] get_lightnings_by_date_between(min_date, max_date)

Get lightnings by date between

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import openapi_client
from api.service import lightnings_api
from openapi_client.model.lightning import Lightning
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
    api_instance = lightnings_api.LightningsApi(api_client)
    min_date = 1 # int | Min date
    max_date = 1 # int | Max date

    # example passing only required values which don't have defaults set
    try:
        # Get lightnings by date between
        api_response = api_instance.get_lightnings_by_date_between(min_date, max_date)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling LightningsApi->get_lightnings_by_date_between: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **min_date** | **int**| Min date |
 **max_date** | **int**| Max date |

### Return type

[**[Lightning]**](Lightning.md)

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

# **get_lightnings_by_date_between_and_disband_id**
> [Lightning] get_lightnings_by_date_between_and_disband_id(min_date, max_date, disband_id)

Get lightnings by date between and disband ID

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import openapi_client
from api.service import lightnings_api
from openapi_client.model.lightning import Lightning
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
    api_instance = lightnings_api.LightningsApi(api_client)
    min_date = 1 # int | Min date
    max_date = 1 # int | Max date
    disband_id = "disbandId_example" # str | Disband ID

    # example passing only required values which don't have defaults set
    try:
        # Get lightnings by date between and disband ID
        api_response = api_instance.get_lightnings_by_date_between_and_disband_id(min_date, max_date, disband_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling LightningsApi->get_lightnings_by_date_between_and_disband_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **min_date** | **int**| Min date |
 **max_date** | **int**| Max date |
 **disband_id** | **str**| Disband ID |

### Return type

[**[Lightning]**](Lightning.md)

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

# **get_lightnings_by_disband_id**
> [Lightning] get_lightnings_by_disband_id(disband_id)

Get lightnings by disband ID

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import openapi_client
from api.service import lightnings_api
from openapi_client.model.lightning import Lightning
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
    api_instance = lightnings_api.LightningsApi(api_client)
    disband_id = "disbandId_example" # str | Disband ID

    # example passing only required values which don't have defaults set
    try:
        # Get lightnings by disband ID
        api_response = api_instance.get_lightnings_by_disband_id(disband_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling LightningsApi->get_lightnings_by_disband_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **disband_id** | **str**| Disband ID |

### Return type

[**[Lightning]**](Lightning.md)

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

# **save_lightning**
> Lightning save_lightning(lightning_dto)

Save lightnint

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import openapi_client
from api.service import lightnings_api
from openapi_client.model.lightning import Lightning
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.lightning_dto import LightningDTO
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
    api_instance = lightnings_api.LightningsApi(api_client)
    lightning_dto = LightningDTO(
        lightning=3.14,
        red_lightning=3.14,
        green_lightning=3.14,
        blue_lightning=3.14,
        date=1,
        disband_id="disband_id_example",
    ) # LightningDTO | 

    # example passing only required values which don't have defaults set
    try:
        # Save lightnint
        api_response = api_instance.save_lightning(lightning_dto)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling LightningsApi->save_lightning: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lightning_dto** | [**LightningDTO**](LightningDTO.md)|  |

### Return type

[**Lightning**](Lightning.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | CREATED |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | Not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

