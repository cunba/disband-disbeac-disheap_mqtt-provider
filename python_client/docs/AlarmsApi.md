# openapi_client.AlarmsApi

All URIs are relative to *http://63.33.86.240:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_alarm**](AlarmsApi.md#delete_alarm) | **DELETE** /alarms/{id} | Delete alarm
[**delete_alarms_by_disband_id**](AlarmsApi.md#delete_alarms_by_disband_id) | **DELETE** /alarms/disbands/{disbandId} | Delete alarms by disband ID
[**get_alarms_by_date_between_and_disband_id**](AlarmsApi.md#get_alarms_by_date_between_and_disband_id) | **GET** /alarms/date/between/disbands/{disbandId} | Get alarms by date between and disband ID
[**get_alarms_by_disband_id**](AlarmsApi.md#get_alarms_by_disband_id) | **GET** /alarms/disbands/{disbandId} | Get alarms by disband ID
[**get_by_id9**](AlarmsApi.md#get_by_id9) | **GET** /alarms/{id} | Get alarm by ID
[**save_alarm**](AlarmsApi.md#save_alarm) | **POST** /alarms | Save alarm
[**update_alarm**](AlarmsApi.md#update_alarm) | **PUT** /alarms/{id} | Update alarm


# **delete_alarm**
> Alarm delete_alarm(id)

Delete alarm

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import openapi_client
from api.service import alarms_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.alarm import Alarm
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
    api_instance = alarms_api.AlarmsApi(api_client)
    id = "id_example" # str | Alarm id

    # example passing only required values which don't have defaults set
    try:
        # Delete alarm
        api_response = api_instance.delete_alarm(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AlarmsApi->delete_alarm: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Alarm id |

### Return type

[**Alarm**](Alarm.md)

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
**404** | Alarm not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_alarms_by_disband_id**
> [Alarm] delete_alarms_by_disband_id(disband_id)

Delete alarms by disband ID

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import openapi_client
from api.service import alarms_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.alarm import Alarm
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
    api_instance = alarms_api.AlarmsApi(api_client)
    disband_id = "disbandId_example" # str | Disband ID

    # example passing only required values which don't have defaults set
    try:
        # Delete alarms by disband ID
        api_response = api_instance.delete_alarms_by_disband_id(disband_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AlarmsApi->delete_alarms_by_disband_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **disband_id** | **str**| Disband ID |

### Return type

[**[Alarm]**](Alarm.md)

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

# **get_alarms_by_date_between_and_disband_id**
> [Alarm] get_alarms_by_date_between_and_disband_id(min_date, max_date, disband_id)

Get alarms by date between and disband ID

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import openapi_client
from api.service import alarms_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.alarm import Alarm
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
    api_instance = alarms_api.AlarmsApi(api_client)
    min_date = 1 # int | Min date
    max_date = 1 # int | Max date
    disband_id = "disbandId_example" # str | Disband ID

    # example passing only required values which don't have defaults set
    try:
        # Get alarms by date between and disband ID
        api_response = api_instance.get_alarms_by_date_between_and_disband_id(min_date, max_date, disband_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AlarmsApi->get_alarms_by_date_between_and_disband_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **min_date** | **int**| Min date |
 **max_date** | **int**| Max date |
 **disband_id** | **str**| Disband ID |

### Return type

[**[Alarm]**](Alarm.md)

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

# **get_alarms_by_disband_id**
> [Alarm] get_alarms_by_disband_id(disband_id)

Get alarms by disband ID

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import openapi_client
from api.service import alarms_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.alarm import Alarm
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
    api_instance = alarms_api.AlarmsApi(api_client)
    disband_id = "disbandId_example" # str | Disband ID

    # example passing only required values which don't have defaults set
    try:
        # Get alarms by disband ID
        api_response = api_instance.get_alarms_by_disband_id(disband_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AlarmsApi->get_alarms_by_disband_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **disband_id** | **str**| Disband ID |

### Return type

[**[Alarm]**](Alarm.md)

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

# **get_by_id9**
> Alarm get_by_id9(id)

Get alarm by ID

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import openapi_client
from api.service import alarms_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.alarm import Alarm
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
    api_instance = alarms_api.AlarmsApi(api_client)
    id = "id_example" # str | Alarm ID

    # example passing only required values which don't have defaults set
    try:
        # Get alarm by ID
        api_response = api_instance.get_by_id9(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AlarmsApi->get_by_id9: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Alarm ID |

### Return type

[**Alarm**](Alarm.md)

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
**404** | Alarm not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_alarm**
> Alarm save_alarm(alarm_dto)

Save alarm

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import openapi_client
from api.service import alarms_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.alarm_dto import AlarmDTO
from openapi_client.model.alarm import Alarm
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
    api_instance = alarms_api.AlarmsApi(api_client)
    alarm_dto = AlarmDTO(
        date=1,
        is_repetition=True,
        repetition_week_days="repetition_week_days_example",
        disband_id="disband_id_example",
    ) # AlarmDTO | 

    # example passing only required values which don't have defaults set
    try:
        # Save alarm
        api_response = api_instance.save_alarm(alarm_dto)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AlarmsApi->save_alarm: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alarm_dto** | [**AlarmDTO**](AlarmDTO.md)|  |

### Return type

[**Alarm**](Alarm.md)

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
**404** | Disband not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_alarm**
> str update_alarm(id, alarm_dto)

Update alarm

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import openapi_client
from api.service import alarms_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.alarm_dto import AlarmDTO
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
    api_instance = alarms_api.AlarmsApi(api_client)
    id = "id_example" # str | Alarm id
    alarm_dto = AlarmDTO(
        date=1,
        is_repetition=True,
        repetition_week_days="repetition_week_days_example",
        disband_id="disband_id_example",
    ) # AlarmDTO | 

    # example passing only required values which don't have defaults set
    try:
        # Update alarm
        api_response = api_instance.update_alarm(id, alarm_dto)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AlarmsApi->update_alarm: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Alarm id |
 **alarm_dto** | [**AlarmDTO**](AlarmDTO.md)|  |

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
**404** | Alarm not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

