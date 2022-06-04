# openapi_client.AmbientNoisesApi

All URIs are relative to *http://63.33.86.240:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_ambient_noises_by_disband_id**](AmbientNoisesApi.md#delete_ambient_noises_by_disband_id) | **DELETE** /ambient-noises/disbands/{disbandId} | Delete ambient noises by disband ID
[**get_all_ambient_noise**](AmbientNoisesApi.md#get_all_ambient_noise) | **GET** /ambient-noises | Get all ambient noises
[**get_ambient_noises_by_date_between**](AmbientNoisesApi.md#get_ambient_noises_by_date_between) | **GET** /ambient-noises/date/between | Get ambient noises by date between
[**get_ambient_noises_by_date_between_and_disband_id**](AmbientNoisesApi.md#get_ambient_noises_by_date_between_and_disband_id) | **GET** /ambient-noises/date/between/disband/{disbandId} | Get ambient noises by date between and disband ID
[**get_ambient_noises_by_disband_id**](AmbientNoisesApi.md#get_ambient_noises_by_disband_id) | **GET** /ambient-noises/disbands/{disbandId} | Get Ambient noises by disband ID
[**get_by_id8**](AmbientNoisesApi.md#get_by_id8) | **GET** /ambient-noises/{id} | Get ambient noise by ID
[**save_ambient_noise**](AmbientNoisesApi.md#save_ambient_noise) | **POST** /ambient-noises | Save ambient noise


# **delete_ambient_noises_by_disband_id**
> [AmbientNoise] delete_ambient_noises_by_disband_id(disband_id)

Delete ambient noises by disband ID

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import openapi_client
from api.service import ambient_noises_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.ambient_noise import AmbientNoise
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
    api_instance = ambient_noises_api.AmbientNoisesApi(api_client)
    disband_id = "disbandId_example" # str | Disband id

    # example passing only required values which don't have defaults set
    try:
        # Delete ambient noises by disband ID
        api_response = api_instance.delete_ambient_noises_by_disband_id(disband_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AmbientNoisesApi->delete_ambient_noises_by_disband_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **disband_id** | **str**| Disband id |

### Return type

[**[AmbientNoise]**](AmbientNoise.md)

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

# **get_all_ambient_noise**
> [AmbientNoise] get_all_ambient_noise()

Get all ambient noises

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import openapi_client
from api.service import ambient_noises_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.ambient_noise import AmbientNoise
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
    api_instance = ambient_noises_api.AmbientNoisesApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get all ambient noises
        api_response = api_instance.get_all_ambient_noise()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AmbientNoisesApi->get_all_ambient_noise: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[AmbientNoise]**](AmbientNoise.md)

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

# **get_ambient_noises_by_date_between**
> [AmbientNoise] get_ambient_noises_by_date_between(min_date, max_date)

Get ambient noises by date between

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import openapi_client
from api.service import ambient_noises_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.ambient_noise import AmbientNoise
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
    api_instance = ambient_noises_api.AmbientNoisesApi(api_client)
    min_date = 1 # int | Min date
    max_date = 1 # int | Max date

    # example passing only required values which don't have defaults set
    try:
        # Get ambient noises by date between
        api_response = api_instance.get_ambient_noises_by_date_between(min_date, max_date)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AmbientNoisesApi->get_ambient_noises_by_date_between: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **min_date** | **int**| Min date |
 **max_date** | **int**| Max date |

### Return type

[**[AmbientNoise]**](AmbientNoise.md)

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

# **get_ambient_noises_by_date_between_and_disband_id**
> [AmbientNoise] get_ambient_noises_by_date_between_and_disband_id(min_date, max_date, disband_id)

Get ambient noises by date between and disband ID

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import openapi_client
from api.service import ambient_noises_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.ambient_noise import AmbientNoise
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
    api_instance = ambient_noises_api.AmbientNoisesApi(api_client)
    min_date = 1 # int | Min date
    max_date = 1 # int | Max date
    disband_id = "disbandId_example" # str | Disband ID

    # example passing only required values which don't have defaults set
    try:
        # Get ambient noises by date between and disband ID
        api_response = api_instance.get_ambient_noises_by_date_between_and_disband_id(min_date, max_date, disband_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AmbientNoisesApi->get_ambient_noises_by_date_between_and_disband_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **min_date** | **int**| Min date |
 **max_date** | **int**| Max date |
 **disband_id** | **str**| Disband ID |

### Return type

[**[AmbientNoise]**](AmbientNoise.md)

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

# **get_ambient_noises_by_disband_id**
> [AmbientNoise] get_ambient_noises_by_disband_id(disband_id)

Get Ambient noises by disband ID

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import openapi_client
from api.service import ambient_noises_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.ambient_noise import AmbientNoise
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
    api_instance = ambient_noises_api.AmbientNoisesApi(api_client)
    disband_id = "disbandId_example" # str | Disband ID

    # example passing only required values which don't have defaults set
    try:
        # Get Ambient noises by disband ID
        api_response = api_instance.get_ambient_noises_by_disband_id(disband_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AmbientNoisesApi->get_ambient_noises_by_disband_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **disband_id** | **str**| Disband ID |

### Return type

[**[AmbientNoise]**](AmbientNoise.md)

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

# **get_by_id8**
> AmbientNoise get_by_id8(id)

Get ambient noise by ID

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import openapi_client
from api.service import ambient_noises_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.ambient_noise import AmbientNoise
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
    api_instance = ambient_noises_api.AmbientNoisesApi(api_client)
    id = "id_example" # str | Ambient noise ID

    # example passing only required values which don't have defaults set
    try:
        # Get ambient noise by ID
        api_response = api_instance.get_by_id8(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AmbientNoisesApi->get_by_id8: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Ambient noise ID |

### Return type

[**AmbientNoise**](AmbientNoise.md)

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

# **save_ambient_noise**
> AmbientNoise save_ambient_noise(measure_dto)

Save ambient noise

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import openapi_client
from api.service import ambient_noises_api
from openapi_client.model.measure_dto import MeasureDTO
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.ambient_noise import AmbientNoise
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
    api_instance = ambient_noises_api.AmbientNoisesApi(api_client)
    measure_dto = MeasureDTO(
        data=3.14,
        date=1,
        disband_mac="disband_mac_example",
    ) # MeasureDTO | 

    # example passing only required values which don't have defaults set
    try:
        # Save ambient noise
        api_response = api_instance.save_ambient_noise(measure_dto)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AmbientNoisesApi->save_ambient_noise: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **measure_dto** | [**MeasureDTO**](MeasureDTO.md)|  |

### Return type

[**AmbientNoise**](AmbientNoise.md)

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

