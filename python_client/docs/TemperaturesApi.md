# openapi_client.TemperaturesApi

All URIs are relative to *http://63.33.86.240:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_temperatures_by_disband_id**](TemperaturesApi.md#delete_temperatures_by_disband_id) | **DELETE** /temperatures/disbands/{disbandId} | Delete temperatures by disband ID
[**get_all_temperature**](TemperaturesApi.md#get_all_temperature) | **GET** /temperatures | Get all temperatures
[**get_by_id**](TemperaturesApi.md#get_by_id) | **GET** /temperatures/{id} | Get temperature by ID
[**get_temperatures_by_date_between**](TemperaturesApi.md#get_temperatures_by_date_between) | **GET** /temperatures/date/between | Get temperatures by date between
[**get_temperatures_by_date_between_and_disband_id**](TemperaturesApi.md#get_temperatures_by_date_between_and_disband_id) | **GET** /temperatures/date/between/disband/{disbandId} | Get temperatures by date between and disband ID
[**get_temperatures_by_disband_id**](TemperaturesApi.md#get_temperatures_by_disband_id) | **GET** /temperatures/disbands/{disbandId} | Get temperatures by disband ID
[**save_temperature**](TemperaturesApi.md#save_temperature) | **POST** /temperatures | Save temperature


# **delete_temperatures_by_disband_id**
> [Temperature] delete_temperatures_by_disband_id(disband_id)

Delete temperatures by disband ID

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import openapi_client
from api.service import temperatures_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.temperature import Temperature
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
    api_instance = temperatures_api.TemperaturesApi(api_client)
    disband_id = "disbandId_example" # str | Disband id

    # example passing only required values which don't have defaults set
    try:
        # Delete temperatures by disband ID
        api_response = api_instance.delete_temperatures_by_disband_id(disband_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TemperaturesApi->delete_temperatures_by_disband_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **disband_id** | **str**| Disband id |

### Return type

[**[Temperature]**](Temperature.md)

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

# **get_all_temperature**
> [Temperature] get_all_temperature()

Get all temperatures

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import openapi_client
from api.service import temperatures_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.temperature import Temperature
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
    api_instance = temperatures_api.TemperaturesApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get all temperatures
        api_response = api_instance.get_all_temperature()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TemperaturesApi->get_all_temperature: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[Temperature]**](Temperature.md)

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

# **get_by_id**
> Temperature get_by_id(id)

Get temperature by ID

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import openapi_client
from api.service import temperatures_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.temperature import Temperature
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
    api_instance = temperatures_api.TemperaturesApi(api_client)
    id = "id_example" # str | Temperature ID

    # example passing only required values which don't have defaults set
    try:
        # Get temperature by ID
        api_response = api_instance.get_by_id(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TemperaturesApi->get_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Temperature ID |

### Return type

[**Temperature**](Temperature.md)

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

# **get_temperatures_by_date_between**
> [Temperature] get_temperatures_by_date_between(min_date, max_date)

Get temperatures by date between

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import openapi_client
from api.service import temperatures_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.temperature import Temperature
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
    api_instance = temperatures_api.TemperaturesApi(api_client)
    min_date = 1 # int | Min date
    max_date = 1 # int | Max date

    # example passing only required values which don't have defaults set
    try:
        # Get temperatures by date between
        api_response = api_instance.get_temperatures_by_date_between(min_date, max_date)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TemperaturesApi->get_temperatures_by_date_between: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **min_date** | **int**| Min date |
 **max_date** | **int**| Max date |

### Return type

[**[Temperature]**](Temperature.md)

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

# **get_temperatures_by_date_between_and_disband_id**
> [Temperature] get_temperatures_by_date_between_and_disband_id(min_date, max_date, disband_id)

Get temperatures by date between and disband ID

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import openapi_client
from api.service import temperatures_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.temperature import Temperature
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
    api_instance = temperatures_api.TemperaturesApi(api_client)
    min_date = 1 # int | Min date
    max_date = 1 # int | Max date
    disband_id = "disbandId_example" # str | Disband ID

    # example passing only required values which don't have defaults set
    try:
        # Get temperatures by date between and disband ID
        api_response = api_instance.get_temperatures_by_date_between_and_disband_id(min_date, max_date, disband_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TemperaturesApi->get_temperatures_by_date_between_and_disband_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **min_date** | **int**| Min date |
 **max_date** | **int**| Max date |
 **disband_id** | **str**| Disband ID |

### Return type

[**[Temperature]**](Temperature.md)

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

# **get_temperatures_by_disband_id**
> [Temperature] get_temperatures_by_disband_id(disband_id)

Get temperatures by disband ID

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import openapi_client
from api.service import temperatures_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.temperature import Temperature
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
    api_instance = temperatures_api.TemperaturesApi(api_client)
    disband_id = "disbandId_example" # str | Disband ID

    # example passing only required values which don't have defaults set
    try:
        # Get temperatures by disband ID
        api_response = api_instance.get_temperatures_by_disband_id(disband_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TemperaturesApi->get_temperatures_by_disband_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **disband_id** | **str**| Disband ID |

### Return type

[**[Temperature]**](Temperature.md)

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

# **save_temperature**
> Temperature save_temperature(measure_dto)

Save temperature

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import openapi_client
from api.service import temperatures_api
from openapi_client.model.measure_dto import MeasureDTO
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.temperature import Temperature
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
    api_instance = temperatures_api.TemperaturesApi(api_client)
    measure_dto = MeasureDTO(
        data=3.14,
        date=1,
        disband_mac="disband_mac_example",
    ) # MeasureDTO | 

    # example passing only required values which don't have defaults set
    try:
        # Save temperature
        api_response = api_instance.save_temperature(measure_dto)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TemperaturesApi->save_temperature: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **measure_dto** | [**MeasureDTO**](MeasureDTO.md)|  |

### Return type

[**Temperature**](Temperature.md)

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

