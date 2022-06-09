# openapi_client.EventsApi

All URIs are relative to *http://63.33.86.240:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_event**](EventsApi.md#delete_event) | **DELETE** /events/{id} | Delete event
[**delete_events_by_user_id**](EventsApi.md#delete_events_by_user_id) | **DELETE** /events/users/{userId} | Delete events by user ID
[**get_event_by_id**](EventsApi.md#get_event_by_id) | **GET** /events/{id} | Get event by ID
[**get_events_by_date_between_and_user_id**](EventsApi.md#get_events_by_date_between_and_user_id) | **GET** /events/date/between/users/{userId} | Get events by date between and user ID
[**get_events_by_type_and_user_id**](EventsApi.md#get_events_by_type_and_user_id) | **GET** /events/types/{type}/users/{userId} | Get events by type and user ID
[**get_events_by_user_id**](EventsApi.md#get_events_by_user_id) | **GET** /events/users/{userId} | Get events by user ID
[**save_event**](EventsApi.md#save_event) | **POST** /events | Save event
[**update_event**](EventsApi.md#update_event) | **PUT** /events/{id} | Update event


# **delete_event**
> Event delete_event(id)

Delete event

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import openapi_client
from api.service import events_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.event import Event
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
    api_instance = events_api.EventsApi(api_client)
    id = "id_example" # str | Event ID

    # example passing only required values which don't have defaults set
    try:
        # Delete event
        api_response = api_instance.delete_event(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling EventsApi->delete_event: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Event ID |

### Return type

[**Event**](Event.md)

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
**404** | Event not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_events_by_user_id**
> [Event] delete_events_by_user_id(user_id)

Delete events by user ID

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import openapi_client
from api.service import events_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.event import Event
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
    api_instance = events_api.EventsApi(api_client)
    user_id = "userId_example" # str | User ID

    # example passing only required values which don't have defaults set
    try:
        # Delete events by user ID
        api_response = api_instance.delete_events_by_user_id(user_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling EventsApi->delete_events_by_user_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User ID |

### Return type

[**[Event]**](Event.md)

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

# **get_event_by_id**
> Event get_event_by_id(id)

Get event by ID

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import openapi_client
from api.service import events_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.event import Event
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
    api_instance = events_api.EventsApi(api_client)
    id = "id_example" # str | Event ID

    # example passing only required values which don't have defaults set
    try:
        # Get event by ID
        api_response = api_instance.get_event_by_id(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling EventsApi->get_event_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Event ID |

### Return type

[**Event**](Event.md)

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
**404** | Event not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_events_by_date_between_and_user_id**
> [Event] get_events_by_date_between_and_user_id(min_date, max_date, user_id)

Get events by date between and user ID

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import openapi_client
from api.service import events_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.event import Event
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
    api_instance = events_api.EventsApi(api_client)
    min_date = 1 # int | Min date
    max_date = 1 # int | Max date
    user_id = "userId_example" # str | User ID

    # example passing only required values which don't have defaults set
    try:
        # Get events by date between and user ID
        api_response = api_instance.get_events_by_date_between_and_user_id(min_date, max_date, user_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling EventsApi->get_events_by_date_between_and_user_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **min_date** | **int**| Min date |
 **max_date** | **int**| Max date |
 **user_id** | **str**| User ID |

### Return type

[**[Event]**](Event.md)

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

# **get_events_by_type_and_user_id**
> [Event] get_events_by_type_and_user_id(type, user_id)

Get events by type and user ID

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import openapi_client
from api.service import events_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.event import Event
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
    api_instance = events_api.EventsApi(api_client)
    type = "type_example" # str | Type
    user_id = "userId_example" # str | User ID

    # example passing only required values which don't have defaults set
    try:
        # Get events by type and user ID
        api_response = api_instance.get_events_by_type_and_user_id(type, user_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling EventsApi->get_events_by_type_and_user_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Type |
 **user_id** | **str**| User ID |

### Return type

[**[Event]**](Event.md)

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

# **get_events_by_user_id**
> [Event] get_events_by_user_id(user_id)

Get events by user ID

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import openapi_client
from api.service import events_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.event import Event
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
    api_instance = events_api.EventsApi(api_client)
    user_id = "userId_example" # str | User ID

    # example passing only required values which don't have defaults set
    try:
        # Get events by user ID
        api_response = api_instance.get_events_by_user_id(user_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling EventsApi->get_events_by_user_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User ID |

### Return type

[**[Event]**](Event.md)

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

# **save_event**
> Event save_event(event_dto)

Save event

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import openapi_client
from api.service import events_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.event_dto import EventDTO
from openapi_client.model.event import Event
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
    api_instance = events_api.EventsApi(api_client)
    event_dto = EventDTO(
        name="name_example",
        notes="notes_example",
        start_date=1,
        end_date=1,
        type="type_example",
        user_id="user_id_example",
    ) # EventDTO | 

    # example passing only required values which don't have defaults set
    try:
        # Save event
        api_response = api_instance.save_event(event_dto)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling EventsApi->save_event: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_dto** | [**EventDTO**](EventDTO.md)|  |

### Return type

[**Event**](Event.md)

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

# **update_event**
> str update_event(id, event_dto)

Update event

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import openapi_client
from api.service import events_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.event_dto import EventDTO
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
    api_instance = events_api.EventsApi(api_client)
    id = "id_example" # str | Event id
    event_dto = EventDTO(
        name="name_example",
        notes="notes_example",
        start_date=1,
        end_date=1,
        type="type_example",
        user_id="user_id_example",
    ) # EventDTO | 

    # example passing only required values which don't have defaults set
    try:
        # Update event
        api_response = api_instance.update_event(id, event_dto)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling EventsApi->update_event: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Event id |
 **event_dto** | [**EventDTO**](EventDTO.md)|  |

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
**404** | Event not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

