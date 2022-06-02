# openapi_client.OxygenApi

All URIs are relative to *http://63.33.86.240:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_oxygens_by_disband_id**](OxygenApi.md#delete_oxygens_by_disband_id) | **DELETE** /oxygens/disbands/{disbandId} | Delete oxygens by disband ID
[**get_all_oxygen**](OxygenApi.md#get_all_oxygen) | **GET** /oxygens | Get all oxygens
[**get_by_id2**](OxygenApi.md#get_by_id2) | **GET** /oxygens/{id} | Get oxygen by ID
[**get_oxygens_by_date_between**](OxygenApi.md#get_oxygens_by_date_between) | **GET** /oxygens/date/between | Get oxygens by date between
[**get_oxygens_by_date_between_and_disband_id**](OxygenApi.md#get_oxygens_by_date_between_and_disband_id) | **GET** /oxygens/date/between/disband/{disbandId} | Get oxygens by date between and disband ID
[**get_oxygens_by_disband_id**](OxygenApi.md#get_oxygens_by_disband_id) | **GET** /oxygens/disbands/{disbandId} | Get oxygens by disband ID
[**save_oxygen**](OxygenApi.md#save_oxygen) | **POST** /oxygens | Save oxygen


# **delete_oxygens_by_disband_id**
> [Oxygen] delete_oxygens_by_disband_id(disband_id)

Delete oxygens by disband ID

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import openapi_client
from api.service import oxygen_api
from openapi_client.model.oxygen import Oxygen
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
    api_instance = oxygen_api.OxygenApi(api_client)
    disband_id = "disbandId_example" # str | Disband id

    # example passing only required values which don't have defaults set
    try:
        # Delete oxygens by disband ID
        api_response = api_instance.delete_oxygens_by_disband_id(disband_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OxygenApi->delete_oxygens_by_disband_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **disband_id** | **str**| Disband id |

### Return type

[**[Oxygen]**](Oxygen.md)

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

# **get_all_oxygen**
> [Oxygen] get_all_oxygen()

Get all oxygens

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import openapi_client
from api.service import oxygen_api
from openapi_client.model.oxygen import Oxygen
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
    api_instance = oxygen_api.OxygenApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get all oxygens
        api_response = api_instance.get_all_oxygen()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OxygenApi->get_all_oxygen: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[Oxygen]**](Oxygen.md)

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

# **get_by_id2**
> Oxygen get_by_id2(id)

Get oxygen by ID

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import openapi_client
from api.service import oxygen_api
from openapi_client.model.oxygen import Oxygen
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
    api_instance = oxygen_api.OxygenApi(api_client)
    id = "id_example" # str | Oxygen ID

    # example passing only required values which don't have defaults set
    try:
        # Get oxygen by ID
        api_response = api_instance.get_by_id2(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OxygenApi->get_by_id2: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Oxygen ID |

### Return type

[**Oxygen**](Oxygen.md)

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

# **get_oxygens_by_date_between**
> [Oxygen] get_oxygens_by_date_between(min_date, max_date)

Get oxygens by date between

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import openapi_client
from api.service import oxygen_api
from openapi_client.model.oxygen import Oxygen
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
    api_instance = oxygen_api.OxygenApi(api_client)
    min_date = 1 # int | Min date
    max_date = 1 # int | Max date

    # example passing only required values which don't have defaults set
    try:
        # Get oxygens by date between
        api_response = api_instance.get_oxygens_by_date_between(min_date, max_date)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OxygenApi->get_oxygens_by_date_between: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **min_date** | **int**| Min date |
 **max_date** | **int**| Max date |

### Return type

[**[Oxygen]**](Oxygen.md)

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

# **get_oxygens_by_date_between_and_disband_id**
> [Oxygen] get_oxygens_by_date_between_and_disband_id(min_date, max_date, disband_id)

Get oxygens by date between and disband ID

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import openapi_client
from api.service import oxygen_api
from openapi_client.model.oxygen import Oxygen
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
    api_instance = oxygen_api.OxygenApi(api_client)
    min_date = 1 # int | Min date
    max_date = 1 # int | Max date
    disband_id = "disbandId_example" # str | Disband ID

    # example passing only required values which don't have defaults set
    try:
        # Get oxygens by date between and disband ID
        api_response = api_instance.get_oxygens_by_date_between_and_disband_id(min_date, max_date, disband_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OxygenApi->get_oxygens_by_date_between_and_disband_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **min_date** | **int**| Min date |
 **max_date** | **int**| Max date |
 **disband_id** | **str**| Disband ID |

### Return type

[**[Oxygen]**](Oxygen.md)

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

# **get_oxygens_by_disband_id**
> [Oxygen] get_oxygens_by_disband_id(disband_id)

Get oxygens by disband ID

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import openapi_client
from api.service import oxygen_api
from openapi_client.model.oxygen import Oxygen
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
    api_instance = oxygen_api.OxygenApi(api_client)
    disband_id = "disbandId_example" # str | Disband ID

    # example passing only required values which don't have defaults set
    try:
        # Get oxygens by disband ID
        api_response = api_instance.get_oxygens_by_disband_id(disband_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OxygenApi->get_oxygens_by_disband_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **disband_id** | **str**| Disband ID |

### Return type

[**[Oxygen]**](Oxygen.md)

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

# **save_oxygen**
> Oxygen save_oxygen(measure_dto)

Save oxygen

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import openapi_client
from api.service import oxygen_api
from openapi_client.model.measure_dto import MeasureDTO
from openapi_client.model.oxygen import Oxygen
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
    api_instance = oxygen_api.OxygenApi(api_client)
    measure_dto = MeasureDTO(
        data=3.14,
        date=1,
        disband_id="disband_id_example",
    ) # MeasureDTO | 

    # example passing only required values which don't have defaults set
    try:
        # Save oxygen
        api_response = api_instance.save_oxygen(measure_dto)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OxygenApi->save_oxygen: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **measure_dto** | [**MeasureDTO**](MeasureDTO.md)|  |

### Return type

[**Oxygen**](Oxygen.md)

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

