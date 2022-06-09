# openapi_client.LocationsApi

All URIs are relative to *http://63.33.86.240:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_location**](LocationsApi.md#delete_location) | **DELETE** /locations/{id} | Delete location by id
[**delete_locations_by_disbeac_id**](LocationsApi.md#delete_locations_by_disbeac_id) | **DELETE** /locations/disbeac/{disbeacId} | Delete all locations by disbeac ID
[**get_all_locations**](LocationsApi.md#get_all_locations) | **GET** /locations | Get all locations
[**get_last1_location_by_date_between_and_disbeac_id**](LocationsApi.md#get_last1_location_by_date_between_and_disbeac_id) | **GET** /locations/last/disbeacId/{disbeacId} | Get last location by disbeac ID
[**get_location_by_id**](LocationsApi.md#get_location_by_id) | **GET** /locations/{id} | Get location by ID
[**get_locations_by_date_between_and_disbeac_id**](LocationsApi.md#get_locations_by_date_between_and_disbeac_id) | **GET** /locations/date/between/disbeacId/{disbeacId} | Get location by date between and disbeac ID
[**get_locations_by_disbeac_id**](LocationsApi.md#get_locations_by_disbeac_id) | **GET** /locations/disbeacId/{disbeacId} | Get location by disbeac ID
[**save_location**](LocationsApi.md#save_location) | **POST** /locations | Save location


# **delete_location**
> Location delete_location(id)

Delete location by id

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import openapi_client
from api.service import locations_api
from openapi_client.model.location import Location
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
    api_instance = locations_api.LocationsApi(api_client)
    id = "id_example" # str | Location ID

    # example passing only required values which don't have defaults set
    try:
        # Delete location by id
        api_response = api_instance.delete_location(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling LocationsApi->delete_location: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Location ID |

### Return type

[**Location**](Location.md)

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
**404** | Location not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_locations_by_disbeac_id**
> [Location] delete_locations_by_disbeac_id(disbeac_id)

Delete all locations by disbeac ID

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import openapi_client
from api.service import locations_api
from openapi_client.model.location import Location
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
    api_instance = locations_api.LocationsApi(api_client)
    disbeac_id = "disbeacId_example" # str | Disbeac ID

    # example passing only required values which don't have defaults set
    try:
        # Delete all locations by disbeac ID
        api_response = api_instance.delete_locations_by_disbeac_id(disbeac_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling LocationsApi->delete_locations_by_disbeac_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **disbeac_id** | **str**| Disbeac ID |

### Return type

[**[Location]**](Location.md)

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

# **get_all_locations**
> [Location] get_all_locations()

Get all locations

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import openapi_client
from api.service import locations_api
from openapi_client.model.location import Location
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
    api_instance = locations_api.LocationsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get all locations
        api_response = api_instance.get_all_locations()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling LocationsApi->get_all_locations: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[Location]**](Location.md)

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

# **get_last1_location_by_date_between_and_disbeac_id**
> Location get_last1_location_by_date_between_and_disbeac_id(min_date, max_date, disbeac_id)

Get last location by disbeac ID

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import openapi_client
from api.service import locations_api
from openapi_client.model.location import Location
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
    api_instance = locations_api.LocationsApi(api_client)
    min_date = 1 # int | Min date
    max_date = 1 # int | Max date
    disbeac_id = "disbeacId_example" # str | Disbeac ID

    # example passing only required values which don't have defaults set
    try:
        # Get last location by disbeac ID
        api_response = api_instance.get_last1_location_by_date_between_and_disbeac_id(min_date, max_date, disbeac_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling LocationsApi->get_last1_location_by_date_between_and_disbeac_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **min_date** | **int**| Min date |
 **max_date** | **int**| Max date |
 **disbeac_id** | **str**| Disbeac ID |

### Return type

[**Location**](Location.md)

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

# **get_location_by_id**
> Location get_location_by_id(id)

Get location by ID

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import openapi_client
from api.service import locations_api
from openapi_client.model.location import Location
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
    api_instance = locations_api.LocationsApi(api_client)
    id = "id_example" # str | Disbeac ID

    # example passing only required values which don't have defaults set
    try:
        # Get location by ID
        api_response = api_instance.get_location_by_id(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling LocationsApi->get_location_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Disbeac ID |

### Return type

[**Location**](Location.md)

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

# **get_locations_by_date_between_and_disbeac_id**
> [Location] get_locations_by_date_between_and_disbeac_id(min_date, max_date, disbeac_id)

Get location by date between and disbeac ID

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import openapi_client
from api.service import locations_api
from openapi_client.model.location import Location
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
    api_instance = locations_api.LocationsApi(api_client)
    min_date = 1 # int | Min date
    max_date = 1 # int | Max date
    disbeac_id = "disbeacId_example" # str | Disbeac ID

    # example passing only required values which don't have defaults set
    try:
        # Get location by date between and disbeac ID
        api_response = api_instance.get_locations_by_date_between_and_disbeac_id(min_date, max_date, disbeac_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling LocationsApi->get_locations_by_date_between_and_disbeac_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **min_date** | **int**| Min date |
 **max_date** | **int**| Max date |
 **disbeac_id** | **str**| Disbeac ID |

### Return type

[**[Location]**](Location.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_locations_by_disbeac_id**
> [Location] get_locations_by_disbeac_id(disbeac_id)

Get location by disbeac ID

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import openapi_client
from api.service import locations_api
from openapi_client.model.location import Location
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
    api_instance = locations_api.LocationsApi(api_client)
    disbeac_id = "disbeacId_example" # str | Disbeac ID

    # example passing only required values which don't have defaults set
    try:
        # Get location by disbeac ID
        api_response = api_instance.get_locations_by_disbeac_id(disbeac_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling LocationsApi->get_locations_by_disbeac_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **disbeac_id** | **str**| Disbeac ID |

### Return type

[**[Location]**](Location.md)

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

# **save_location**
> Location save_location()

Save location

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import openapi_client
from api.service import locations_api
from openapi_client.model.location_dto import LocationDTO
from openapi_client.model.location import Location
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
    api_instance = locations_api.LocationsApi(api_client)
    location_dto = LocationDTO(
        latitude=3.14,
        longitude=3.14,
        date=1,
        disbeac_mac="disbeac_mac_example",
    ) # LocationDTO |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Save location
        api_response = api_instance.save_location(location_dto=location_dto)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling LocationsApi->save_location: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_dto** | [**LocationDTO**](LocationDTO.md)|  | [optional]

### Return type

[**Location**](Location.md)

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
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

