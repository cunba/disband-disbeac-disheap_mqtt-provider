# openapi_client.DisordersApi

All URIs are relative to *http://63.33.86.240:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_all_disorders**](DisordersApi.md#delete_all_disorders) | **DELETE** /disorders | Delete all disorders
[**delete_disorder**](DisordersApi.md#delete_disorder) | **DELETE** /disorders/{id} | Delete disorder
[**get_all_disorders**](DisordersApi.md#get_all_disorders) | **GET** /disorders | Get all disorders
[**get_disorder_by_id**](DisordersApi.md#get_disorder_by_id) | **GET** /disorders/{id} | Get disorder by ID
[**save_disorder**](DisordersApi.md#save_disorder) | **POST** /disorders | Save disorder
[**update_disorder**](DisordersApi.md#update_disorder) | **PUT** /disorders/{id} | Update disorder


# **delete_all_disorders**
> [Disorder] delete_all_disorders()

Delete all disorders

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import openapi_client
from api.service import disorders_api
from openapi_client.model.disorder import Disorder
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
    api_instance = disorders_api.DisordersApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Delete all disorders
        api_response = api_instance.delete_all_disorders()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DisordersApi->delete_all_disorders: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[Disorder]**](Disorder.md)

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

# **delete_disorder**
> Disorder delete_disorder(id)

Delete disorder

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import openapi_client
from api.service import disorders_api
from openapi_client.model.disorder import Disorder
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
    api_instance = disorders_api.DisordersApi(api_client)
    id = "id_example" # str | Disorder ID

    # example passing only required values which don't have defaults set
    try:
        # Delete disorder
        api_response = api_instance.delete_disorder(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DisordersApi->delete_disorder: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Disorder ID |

### Return type

[**Disorder**](Disorder.md)

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
**404** | Disorder not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_disorders**
> [Disorder] get_all_disorders()

Get all disorders

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import openapi_client
from api.service import disorders_api
from openapi_client.model.disorder import Disorder
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
    api_instance = disorders_api.DisordersApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get all disorders
        api_response = api_instance.get_all_disorders()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DisordersApi->get_all_disorders: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[Disorder]**](Disorder.md)

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

# **get_disorder_by_id**
> Disorder get_disorder_by_id(id)

Get disorder by ID

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import openapi_client
from api.service import disorders_api
from openapi_client.model.disorder import Disorder
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
    api_instance = disorders_api.DisordersApi(api_client)
    id = "id_example" # str | Disorder ID

    # example passing only required values which don't have defaults set
    try:
        # Get disorder by ID
        api_response = api_instance.get_disorder_by_id(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DisordersApi->get_disorder_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Disorder ID |

### Return type

[**Disorder**](Disorder.md)

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

# **save_disorder**
> Disorder save_disorder(disorder_dto)

Save disorder

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import openapi_client
from api.service import disorders_api
from openapi_client.model.disorder import Disorder
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.disorder_dto import DisorderDTO
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
    api_instance = disorders_api.DisordersApi(api_client)
    disorder_dto = DisorderDTO(
        name="name_example",
        observations="observations_example",
    ) # DisorderDTO | 

    # example passing only required values which don't have defaults set
    try:
        # Save disorder
        api_response = api_instance.save_disorder(disorder_dto)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DisordersApi->save_disorder: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **disorder_dto** | [**DisorderDTO**](DisorderDTO.md)|  |

### Return type

[**Disorder**](Disorder.md)

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

# **update_disorder**
> str update_disorder(id, disorder_dto)

Update disorder

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import openapi_client
from api.service import disorders_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.disorder_dto import DisorderDTO
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
    api_instance = disorders_api.DisordersApi(api_client)
    id = "id_example" # str | Disorder id
    disorder_dto = DisorderDTO(
        name="name_example",
        observations="observations_example",
    ) # DisorderDTO | 

    # example passing only required values which don't have defaults set
    try:
        # Update disorder
        api_response = api_instance.update_disorder(id, disorder_dto)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DisordersApi->update_disorder: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Disorder id |
 **disorder_dto** | [**DisorderDTO**](DisorderDTO.md)|  |

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
**404** | Disorder not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

