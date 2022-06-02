# openapi_client.PressureApi

All URIs are relative to *http://63.33.86.240:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_pressures_by_disband_id**](PressureApi.md#delete_pressures_by_disband_id) | **DELETE** /pressures/disbands/{disbandId} | Delete pressures by disband ID
[**get_all_pressure**](PressureApi.md#get_all_pressure) | **GET** /pressures | Get all pressures
[**get_by_id1**](PressureApi.md#get_by_id1) | **GET** /pressures/{id} | Get pressure by ID
[**get_pressures_by_date_between**](PressureApi.md#get_pressures_by_date_between) | **GET** /pressures/date/between | Get pressures by date between
[**get_pressures_by_date_between_and_disband_id**](PressureApi.md#get_pressures_by_date_between_and_disband_id) | **GET** /pressures/date/between/disband/{disbandId} | Get pressures by date between and disband ID
[**get_pressures_by_disband_id**](PressureApi.md#get_pressures_by_disband_id) | **GET** /pressures/disbands/{disbandId} | Get pressures by disband ID
[**save_pressure**](PressureApi.md#save_pressure) | **POST** /pressures | Save pressure


# **delete_pressures_by_disband_id**
> [Pressure] delete_pressures_by_disband_id(disband_id)

Delete pressures by disband ID

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import openapi_client
from api.service import pressure_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.pressure import Pressure
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
    api_instance = pressure_api.PressureApi(api_client)
    disband_id = "disbandId_example" # str | Disband id

    # example passing only required values which don't have defaults set
    try:
        # Delete pressures by disband ID
        api_response = api_instance.delete_pressures_by_disband_id(disband_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PressureApi->delete_pressures_by_disband_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **disband_id** | **str**| Disband id |

### Return type

[**[Pressure]**](Pressure.md)

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

# **get_all_pressure**
> [Pressure] get_all_pressure()

Get all pressures

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import openapi_client
from api.service import pressure_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.pressure import Pressure
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
    api_instance = pressure_api.PressureApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get all pressures
        api_response = api_instance.get_all_pressure()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PressureApi->get_all_pressure: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[Pressure]**](Pressure.md)

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

# **get_by_id1**
> Pressure get_by_id1(id)

Get pressure by ID

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import openapi_client
from api.service import pressure_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.pressure import Pressure
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
    api_instance = pressure_api.PressureApi(api_client)
    id = "id_example" # str | Pressure ID

    # example passing only required values which don't have defaults set
    try:
        # Get pressure by ID
        api_response = api_instance.get_by_id1(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PressureApi->get_by_id1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Pressure ID |

### Return type

[**Pressure**](Pressure.md)

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

# **get_pressures_by_date_between**
> [Pressure] get_pressures_by_date_between(min_date, max_date)

Get pressures by date between

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import openapi_client
from api.service import pressure_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.pressure import Pressure
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
    api_instance = pressure_api.PressureApi(api_client)
    min_date = 1 # int | Min date
    max_date = 1 # int | Max date

    # example passing only required values which don't have defaults set
    try:
        # Get pressures by date between
        api_response = api_instance.get_pressures_by_date_between(min_date, max_date)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PressureApi->get_pressures_by_date_between: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **min_date** | **int**| Min date |
 **max_date** | **int**| Max date |

### Return type

[**[Pressure]**](Pressure.md)

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

# **get_pressures_by_date_between_and_disband_id**
> [Pressure] get_pressures_by_date_between_and_disband_id(min_date, max_date, disband_id)

Get pressures by date between and disband ID

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import openapi_client
from api.service import pressure_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.pressure import Pressure
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
    api_instance = pressure_api.PressureApi(api_client)
    min_date = 1 # int | Min date
    max_date = 1 # int | Max date
    disband_id = "disbandId_example" # str | Disband ID

    # example passing only required values which don't have defaults set
    try:
        # Get pressures by date between and disband ID
        api_response = api_instance.get_pressures_by_date_between_and_disband_id(min_date, max_date, disband_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PressureApi->get_pressures_by_date_between_and_disband_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **min_date** | **int**| Min date |
 **max_date** | **int**| Max date |
 **disband_id** | **str**| Disband ID |

### Return type

[**[Pressure]**](Pressure.md)

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

# **get_pressures_by_disband_id**
> [Pressure] get_pressures_by_disband_id(disband_id)

Get pressures by disband ID

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import openapi_client
from api.service import pressure_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.pressure import Pressure
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
    api_instance = pressure_api.PressureApi(api_client)
    disband_id = "disbandId_example" # str | Disband ID

    # example passing only required values which don't have defaults set
    try:
        # Get pressures by disband ID
        api_response = api_instance.get_pressures_by_disband_id(disband_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PressureApi->get_pressures_by_disband_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **disband_id** | **str**| Disband ID |

### Return type

[**[Pressure]**](Pressure.md)

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

# **save_pressure**
> Pressure save_pressure(measure_dto)

Save pressure

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import openapi_client
from api.service import pressure_api
from openapi_client.model.measure_dto import MeasureDTO
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.pressure import Pressure
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
    api_instance = pressure_api.PressureApi(api_client)
    measure_dto = MeasureDTO(
        data=3.14,
        date=1,
        disband_id="disband_id_example",
    ) # MeasureDTO | 

    # example passing only required values which don't have defaults set
    try:
        # Save pressure
        api_response = api_instance.save_pressure(measure_dto)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PressureApi->save_pressure: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **measure_dto** | [**MeasureDTO**](MeasureDTO.md)|  |

### Return type

[**Pressure**](Pressure.md)

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

