# openapi_client.HumidityApi

All URIs are relative to *http://63.33.86.240:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_humiditys_by_disband_id**](HumidityApi.md#delete_humiditys_by_disband_id) | **DELETE** /humidities/disbands/{disbandId} | Delete humidities by disband ID
[**get_all_humidity**](HumidityApi.md#get_all_humidity) | **GET** /humidities | Get all humidities
[**get_by_id4**](HumidityApi.md#get_by_id4) | **GET** /humidities/{id} | Get humidity by ID
[**get_humiditys_by_date_between**](HumidityApi.md#get_humiditys_by_date_between) | **GET** /humidities/date/between | Get humidities by date between
[**get_humiditys_by_date_between_and_disband_id**](HumidityApi.md#get_humiditys_by_date_between_and_disband_id) | **GET** /humidities/date/between/disband/{disbandId} | Get humidities by date between and disband ID
[**get_humiditys_by_disband_id**](HumidityApi.md#get_humiditys_by_disband_id) | **GET** /humidities/disbands/{disbandId} | Get humidities by disband ID
[**save_humidity**](HumidityApi.md#save_humidity) | **POST** /humidities | Save humidity


# **delete_humiditys_by_disband_id**
> [Humidity] delete_humiditys_by_disband_id(disband_id)

Delete humidities by disband ID

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import openapi_client
from api.service import humidity_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.humidity import Humidity
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
    api_instance = humidity_api.HumidityApi(api_client)
    disband_id = "disbandId_example" # str | Disband id

    # example passing only required values which don't have defaults set
    try:
        # Delete humidities by disband ID
        api_response = api_instance.delete_humiditys_by_disband_id(disband_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling HumidityApi->delete_humiditys_by_disband_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **disband_id** | **str**| Disband id |

### Return type

[**[Humidity]**](Humidity.md)

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

# **get_all_humidity**
> [Humidity] get_all_humidity()

Get all humidities

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import openapi_client
from api.service import humidity_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.humidity import Humidity
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
    api_instance = humidity_api.HumidityApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get all humidities
        api_response = api_instance.get_all_humidity()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling HumidityApi->get_all_humidity: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[Humidity]**](Humidity.md)

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

# **get_by_id4**
> Humidity get_by_id4(id)

Get humidity by ID

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import openapi_client
from api.service import humidity_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.humidity import Humidity
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
    api_instance = humidity_api.HumidityApi(api_client)
    id = "id_example" # str | Humidity ID

    # example passing only required values which don't have defaults set
    try:
        # Get humidity by ID
        api_response = api_instance.get_by_id4(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling HumidityApi->get_by_id4: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Humidity ID |

### Return type

[**Humidity**](Humidity.md)

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

# **get_humiditys_by_date_between**
> [Humidity] get_humiditys_by_date_between(min_date, max_date)

Get humidities by date between

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import openapi_client
from api.service import humidity_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.humidity import Humidity
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
    api_instance = humidity_api.HumidityApi(api_client)
    min_date = 1 # int | Min date
    max_date = 1 # int | Max date

    # example passing only required values which don't have defaults set
    try:
        # Get humidities by date between
        api_response = api_instance.get_humiditys_by_date_between(min_date, max_date)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling HumidityApi->get_humiditys_by_date_between: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **min_date** | **int**| Min date |
 **max_date** | **int**| Max date |

### Return type

[**[Humidity]**](Humidity.md)

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

# **get_humiditys_by_date_between_and_disband_id**
> [Humidity] get_humiditys_by_date_between_and_disband_id(min_date, max_date, disband_id)

Get humidities by date between and disband ID

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import openapi_client
from api.service import humidity_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.humidity import Humidity
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
    api_instance = humidity_api.HumidityApi(api_client)
    min_date = 1 # int | Min date
    max_date = 1 # int | Max date
    disband_id = "disbandId_example" # str | Disband ID

    # example passing only required values which don't have defaults set
    try:
        # Get humidities by date between and disband ID
        api_response = api_instance.get_humiditys_by_date_between_and_disband_id(min_date, max_date, disband_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling HumidityApi->get_humiditys_by_date_between_and_disband_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **min_date** | **int**| Min date |
 **max_date** | **int**| Max date |
 **disband_id** | **str**| Disband ID |

### Return type

[**[Humidity]**](Humidity.md)

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

# **get_humiditys_by_disband_id**
> [Humidity] get_humiditys_by_disband_id(disband_id)

Get humidities by disband ID

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import openapi_client
from api.service import humidity_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.humidity import Humidity
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
    api_instance = humidity_api.HumidityApi(api_client)
    disband_id = "disbandId_example" # str | Disband ID

    # example passing only required values which don't have defaults set
    try:
        # Get humidities by disband ID
        api_response = api_instance.get_humiditys_by_disband_id(disband_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling HumidityApi->get_humiditys_by_disband_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **disband_id** | **str**| Disband ID |

### Return type

[**[Humidity]**](Humidity.md)

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

# **save_humidity**
> Humidity save_humidity(measure_dto)

Save humidity

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import openapi_client
from api.service import humidity_api
from openapi_client.model.measure_dto import MeasureDTO
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.humidity import Humidity
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
    api_instance = humidity_api.HumidityApi(api_client)
    measure_dto = MeasureDTO(
        data=3.14,
        date=1,
        disband_id="disband_id_example",
    ) # MeasureDTO | 

    # example passing only required values which don't have defaults set
    try:
        # Save humidity
        api_response = api_instance.save_humidity(measure_dto)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling HumidityApi->save_humidity: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **measure_dto** | [**MeasureDTO**](MeasureDTO.md)|  |

### Return type

[**Humidity**](Humidity.md)

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

