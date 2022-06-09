# openapi_client.TimetablesApi

All URIs are relative to *http://63.33.86.240:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_timetable**](TimetablesApi.md#delete_timetable) | **DELETE** /timetables/{id} | Delete timetable
[**delete_timetables_by_user_id**](TimetablesApi.md#delete_timetables_by_user_id) | **DELETE** /timetables/users/{userId} | Delete timetables by user ID
[**get_timetable_by_id**](TimetablesApi.md#get_timetable_by_id) | **GET** /timetables/{id} | Get timetable by ID
[**get_timetables_by_user_id**](TimetablesApi.md#get_timetables_by_user_id) | **GET** /timetables/users/{userId} | Get timetables by user ID
[**save_timetable**](TimetablesApi.md#save_timetable) | **POST** /timetables | Save timetable
[**update_timetable**](TimetablesApi.md#update_timetable) | **PUT** /timetables/{id} | Update timetable


# **delete_timetable**
> Timetable delete_timetable(id)

Delete timetable

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import openapi_client
from api.service import timetables_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.timetable import Timetable
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
    api_instance = timetables_api.TimetablesApi(api_client)
    id = "id_example" # str | Timetable ID

    # example passing only required values which don't have defaults set
    try:
        # Delete timetable
        api_response = api_instance.delete_timetable(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TimetablesApi->delete_timetable: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Timetable ID |

### Return type

[**Timetable**](Timetable.md)

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
**404** | Timetable not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_timetables_by_user_id**
> [Timetable] delete_timetables_by_user_id(user_id)

Delete timetables by user ID

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import openapi_client
from api.service import timetables_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.timetable import Timetable
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
    api_instance = timetables_api.TimetablesApi(api_client)
    user_id = "userId_example" # str | User ID

    # example passing only required values which don't have defaults set
    try:
        # Delete timetables by user ID
        api_response = api_instance.delete_timetables_by_user_id(user_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TimetablesApi->delete_timetables_by_user_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User ID |

### Return type

[**[Timetable]**](Timetable.md)

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

# **get_timetable_by_id**
> Timetable get_timetable_by_id(id)

Get timetable by ID

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import openapi_client
from api.service import timetables_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.timetable import Timetable
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
    api_instance = timetables_api.TimetablesApi(api_client)
    id = "id_example" # str | Timetable ID

    # example passing only required values which don't have defaults set
    try:
        # Get timetable by ID
        api_response = api_instance.get_timetable_by_id(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TimetablesApi->get_timetable_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Timetable ID |

### Return type

[**Timetable**](Timetable.md)

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
**404** | Timetable not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_timetables_by_user_id**
> [Timetable] get_timetables_by_user_id(user_id)

Get timetables by user ID

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import openapi_client
from api.service import timetables_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.timetable import Timetable
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
    api_instance = timetables_api.TimetablesApi(api_client)
    user_id = "userId_example" # str | User ID

    # example passing only required values which don't have defaults set
    try:
        # Get timetables by user ID
        api_response = api_instance.get_timetables_by_user_id(user_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TimetablesApi->get_timetables_by_user_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User ID |

### Return type

[**[Timetable]**](Timetable.md)

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

# **save_timetable**
> Timetable save_timetable(timetable_dto)

Save timetable

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import openapi_client
from api.service import timetables_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.timetable import Timetable
from openapi_client.model.timetable_dto import TimetableDTO
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
    api_instance = timetables_api.TimetablesApi(api_client)
    timetable_dto = TimetableDTO(
        start_time="start_time_example",
        end_time="end_time_example",
        week_day=0,
        subject_id="subject_id_example",
        user_id="user_id_example",
    ) # TimetableDTO | 

    # example passing only required values which don't have defaults set
    try:
        # Save timetable
        api_response = api_instance.save_timetable(timetable_dto)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TimetablesApi->save_timetable: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timetable_dto** | [**TimetableDTO**](TimetableDTO.md)|  |

### Return type

[**Timetable**](Timetable.md)

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
**404** | User not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_timetable**
> str update_timetable(id, timetable_dto)

Update timetable

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import openapi_client
from api.service import timetables_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.timetable_dto import TimetableDTO
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
    api_instance = timetables_api.TimetablesApi(api_client)
    id = "id_example" # str | Timetable id
    timetable_dto = TimetableDTO(
        start_time="start_time_example",
        end_time="end_time_example",
        week_day=0,
        subject_id="subject_id_example",
        user_id="user_id_example",
    ) # TimetableDTO | 

    # example passing only required values which don't have defaults set
    try:
        # Update timetable
        api_response = api_instance.update_timetable(id, timetable_dto)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TimetablesApi->update_timetable: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Timetable id |
 **timetable_dto** | [**TimetableDTO**](TimetableDTO.md)|  |

### Return type

**str**

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
**404** | Timetable not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

