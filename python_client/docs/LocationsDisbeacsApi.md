# openapi_client.LocationsDisbeacsApi

All URIs are relative to *http://63.33.86.240:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_by_disbeac_id**](LocationsDisbeacsApi.md#delete_by_disbeac_id) | **DELETE** /locations-disbeacs/disbeac/{disbeacId} | Delete all locations by disbeac ID
[**delete_location**](LocationsDisbeacsApi.md#delete_location) | **DELETE** /locations-disbeacs/{id} | Delete location by id
[**get_all_location**](LocationsDisbeacsApi.md#get_all_location) | **GET** /locations-disbeacs | Get all locations
[**get_last1_by_disbeac_id**](LocationsDisbeacsApi.md#get_last1_by_disbeac_id) | **GET** /locations-disbeacs/last/disbeacId/{disbeacId} | Get last location by disbeac ID
[**get_location_by_date_between_and_disbeac_id**](LocationsDisbeacsApi.md#get_location_by_date_between_and_disbeac_id) | **GET** /locations-disbeacs/date/between/disbeacId/{disbeacId} | Get location by date between and disbeac ID
[**get_location_by_disbeac_id**](LocationsDisbeacsApi.md#get_location_by_disbeac_id) | **GET** /locations-disbeacs/disbeacId/{disbeacId} | Get location by disbeac ID
[**get_location_by_id**](LocationsDisbeacsApi.md#get_location_by_id) | **GET** /locations-disbeacs/{id} | Get location disbeac by ID
[**save_location**](LocationsDisbeacsApi.md#save_location) | **POST** /locations-disbeacs | Save location


# **delete_by_disbeac_id**
> [LocationDisbeac] delete_by_disbeac_id(disbeac_id)

Delete all locations by disbeac ID

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import openapi_client
from api.service import locations_disbeacs_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.location_disbeac import LocationDisbeac
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
    api_instance = locations_disbeacs_api.LocationsDisbeacsApi(api_client)
    disbeac_id = "disbeacId_example" # str | Disbeac ID

    # example passing only required values which don't have defaults set
    try:
        # Delete all locations by disbeac ID
        api_response = api_instance.delete_by_disbeac_id(disbeac_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling LocationsDisbeacsApi->delete_by_disbeac_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **disbeac_id** | **str**| Disbeac ID |

### Return type

[**[LocationDisbeac]**](LocationDisbeac.md)

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

# **delete_location**
> LocationDisbeac delete_location(id)

Delete location by id

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import openapi_client
from api.service import locations_disbeacs_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.location_disbeac import LocationDisbeac
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
    api_instance = locations_disbeacs_api.LocationsDisbeacsApi(api_client)
    id = "id_example" # str | Location ID

    # example passing only required values which don't have defaults set
    try:
        # Delete location by id
        api_response = api_instance.delete_location(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling LocationsDisbeacsApi->delete_location: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Location ID |

### Return type

[**LocationDisbeac**](LocationDisbeac.md)

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

# **get_all_location**
> [LocationDisbeac] get_all_location()

Get all locations

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import openapi_client
from api.service import locations_disbeacs_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.location_disbeac import LocationDisbeac
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
    api_instance = locations_disbeacs_api.LocationsDisbeacsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get all locations
        api_response = api_instance.get_all_location()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling LocationsDisbeacsApi->get_all_location: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[LocationDisbeac]**](LocationDisbeac.md)

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

# **get_last1_by_disbeac_id**
> [LocationDisbeac] get_last1_by_disbeac_id(disbeac_id)

Get last location by disbeac ID

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import openapi_client
from api.service import locations_disbeacs_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.location_disbeac import LocationDisbeac
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
    api_instance = locations_disbeacs_api.LocationsDisbeacsApi(api_client)
    disbeac_id = "disbeacId_example" # str | Disbeac ID

    # example passing only required values which don't have defaults set
    try:
        # Get last location by disbeac ID
        api_response = api_instance.get_last1_by_disbeac_id(disbeac_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling LocationsDisbeacsApi->get_last1_by_disbeac_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **disbeac_id** | **str**| Disbeac ID |

### Return type

[**[LocationDisbeac]**](LocationDisbeac.md)

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

# **get_location_by_date_between_and_disbeac_id**
> [LocationDisbeac] get_location_by_date_between_and_disbeac_id(min_date, max_date, disbeac_id)

Get location by date between and disbeac ID

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import openapi_client
from api.service import locations_disbeacs_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.location_disbeac import LocationDisbeac
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
    api_instance = locations_disbeacs_api.LocationsDisbeacsApi(api_client)
    min_date = 1 # int | Min date
    max_date = 1 # int | Max date
    disbeac_id = "disbeacId_example" # str | Disbeac ID

    # example passing only required values which don't have defaults set
    try:
        # Get location by date between and disbeac ID
        api_response = api_instance.get_location_by_date_between_and_disbeac_id(min_date, max_date, disbeac_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling LocationsDisbeacsApi->get_location_by_date_between_and_disbeac_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **min_date** | **int**| Min date |
 **max_date** | **int**| Max date |
 **disbeac_id** | **str**| Disbeac ID |

### Return type

[**[LocationDisbeac]**](LocationDisbeac.md)

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

# **get_location_by_disbeac_id**
> [LocationDisbeac] get_location_by_disbeac_id(disbeac_id)

Get location by disbeac ID

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import openapi_client
from api.service import locations_disbeacs_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.location_disbeac import LocationDisbeac
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
    api_instance = locations_disbeacs_api.LocationsDisbeacsApi(api_client)
    disbeac_id = "disbeacId_example" # str | Disbeac ID

    # example passing only required values which don't have defaults set
    try:
        # Get location by disbeac ID
        api_response = api_instance.get_location_by_disbeac_id(disbeac_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling LocationsDisbeacsApi->get_location_by_disbeac_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **disbeac_id** | **str**| Disbeac ID |

### Return type

[**[LocationDisbeac]**](LocationDisbeac.md)

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
> LocationDisbeac get_location_by_id(id)

Get location disbeac by ID

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import openapi_client
from api.service import locations_disbeacs_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.location_disbeac import LocationDisbeac
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
    api_instance = locations_disbeacs_api.LocationsDisbeacsApi(api_client)
    id = "id_example" # str | Disbeac ID

    # example passing only required values which don't have defaults set
    try:
        # Get location disbeac by ID
        api_response = api_instance.get_location_by_id(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling LocationsDisbeacsApi->get_location_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Disbeac ID |

### Return type

[**LocationDisbeac**](LocationDisbeac.md)

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

# **save_location**
> LocationDisbeac save_location()

Save location

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import openapi_client
from api.service import locations_disbeacs_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.location_disbeac import LocationDisbeac
from openapi_client.model.location_disbeac_dto import LocationDisbeacDTO
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
    api_instance = locations_disbeacs_api.LocationsDisbeacsApi(api_client)
    location_disbeac_dto = LocationDisbeacDTO(
        latitude=3.14,
        longitude=3.14,
        date=1,
        disbeac_id="disbeac_id_example",
    ) # LocationDisbeacDTO |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Save location
        api_response = api_instance.save_location(location_disbeac_dto=location_disbeac_dto)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling LocationsDisbeacsApi->save_location: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_disbeac_dto** | [**LocationDisbeacDTO**](LocationDisbeacDTO.md)|  | [optional]

### Return type

[**LocationDisbeac**](LocationDisbeac.md)

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

