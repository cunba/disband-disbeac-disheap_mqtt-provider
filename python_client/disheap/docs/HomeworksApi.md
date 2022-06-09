# openapi_client.HomeworksApi

All URIs are relative to *http://63.33.86.240:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_homework**](HomeworksApi.md#delete_homework) | **DELETE** /homeworks/{id} | Delete homework
[**delete_homeworks_by_user_id**](HomeworksApi.md#delete_homeworks_by_user_id) | **DELETE** /homeworks/users/{userId} | Delete homeworks by user ID
[**get_homework_by_id**](HomeworksApi.md#get_homework_by_id) | **GET** /homeworks/{id} | Get homework by ID
[**get_homeworks_by_deadline_between_and_subject_id_and_user_id**](HomeworksApi.md#get_homeworks_by_deadline_between_and_subject_id_and_user_id) | **GET** /homeworks/deadline/between/subjects/{subjectId}/users/{userId} | Get homeworks by deadline between and subject ID and user ID
[**get_homeworks_by_deadline_between_and_user_id**](HomeworksApi.md#get_homeworks_by_deadline_between_and_user_id) | **GET** /homeworks/deadline/between/users/{userId} | Get homeworks by deadline between and user ID
[**get_homeworks_by_user_id**](HomeworksApi.md#get_homeworks_by_user_id) | **GET** /homeworks/users/{userId} | Get homeworks by user ID
[**save_homework**](HomeworksApi.md#save_homework) | **POST** /homeworks | Save homework
[**update_homework**](HomeworksApi.md#update_homework) | **PUT** /homeworks/{id} | Update homework


# **delete_homework**
> Homework delete_homework(id)

Delete homework

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import openapi_client
from api.service import homeworks_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.homework import Homework
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
    api_instance = homeworks_api.HomeworksApi(api_client)
    id = "id_example" # str | Homework ID

    # example passing only required values which don't have defaults set
    try:
        # Delete homework
        api_response = api_instance.delete_homework(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling HomeworksApi->delete_homework: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Homework ID |

### Return type

[**Homework**](Homework.md)

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
**404** | Homework not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_homeworks_by_user_id**
> [Homework] delete_homeworks_by_user_id(user_id)

Delete homeworks by user ID

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import openapi_client
from api.service import homeworks_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.homework import Homework
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
    api_instance = homeworks_api.HomeworksApi(api_client)
    user_id = "userId_example" # str | User ID

    # example passing only required values which don't have defaults set
    try:
        # Delete homeworks by user ID
        api_response = api_instance.delete_homeworks_by_user_id(user_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling HomeworksApi->delete_homeworks_by_user_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User ID |

### Return type

[**[Homework]**](Homework.md)

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

# **get_homework_by_id**
> Homework get_homework_by_id(id)

Get homework by ID

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import openapi_client
from api.service import homeworks_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.homework import Homework
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
    api_instance = homeworks_api.HomeworksApi(api_client)
    id = "id_example" # str | Homework ID

    # example passing only required values which don't have defaults set
    try:
        # Get homework by ID
        api_response = api_instance.get_homework_by_id(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling HomeworksApi->get_homework_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Homework ID |

### Return type

[**Homework**](Homework.md)

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

# **get_homeworks_by_deadline_between_and_subject_id_and_user_id**
> [Homework] get_homeworks_by_deadline_between_and_subject_id_and_user_id(min_date, max_date, subject_id, user_id)

Get homeworks by deadline between and subject ID and user ID

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import openapi_client
from api.service import homeworks_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.homework import Homework
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
    api_instance = homeworks_api.HomeworksApi(api_client)
    min_date = 1 # int | Min date
    max_date = 1 # int | Max date
    subject_id = "subjectId_example" # str | Subject ID
    user_id = "userId_example" # str | User ID

    # example passing only required values which don't have defaults set
    try:
        # Get homeworks by deadline between and subject ID and user ID
        api_response = api_instance.get_homeworks_by_deadline_between_and_subject_id_and_user_id(min_date, max_date, subject_id, user_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling HomeworksApi->get_homeworks_by_deadline_between_and_subject_id_and_user_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **min_date** | **int**| Min date |
 **max_date** | **int**| Max date |
 **subject_id** | **str**| Subject ID |
 **user_id** | **str**| User ID |

### Return type

[**[Homework]**](Homework.md)

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

# **get_homeworks_by_deadline_between_and_user_id**
> [Homework] get_homeworks_by_deadline_between_and_user_id(min_date, max_date, user_id)

Get homeworks by deadline between and user ID

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import openapi_client
from api.service import homeworks_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.homework import Homework
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
    api_instance = homeworks_api.HomeworksApi(api_client)
    min_date = 1 # int | Min date
    max_date = 1 # int | Max date
    user_id = "userId_example" # str | User ID

    # example passing only required values which don't have defaults set
    try:
        # Get homeworks by deadline between and user ID
        api_response = api_instance.get_homeworks_by_deadline_between_and_user_id(min_date, max_date, user_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling HomeworksApi->get_homeworks_by_deadline_between_and_user_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **min_date** | **int**| Min date |
 **max_date** | **int**| Max date |
 **user_id** | **str**| User ID |

### Return type

[**[Homework]**](Homework.md)

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

# **get_homeworks_by_user_id**
> [Homework] get_homeworks_by_user_id(user_id)

Get homeworks by user ID

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import openapi_client
from api.service import homeworks_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.homework import Homework
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
    api_instance = homeworks_api.HomeworksApi(api_client)
    user_id = "userId_example" # str | User ID

    # example passing only required values which don't have defaults set
    try:
        # Get homeworks by user ID
        api_response = api_instance.get_homeworks_by_user_id(user_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling HomeworksApi->get_homeworks_by_user_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User ID |

### Return type

[**[Homework]**](Homework.md)

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

# **save_homework**
> Homework save_homework(homework_dto)

Save homework

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import openapi_client
from api.service import homeworks_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.homework_dto import HomeworkDTO
from openapi_client.model.homework import Homework
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
    api_instance = homeworks_api.HomeworksApi(api_client)
    homework_dto = HomeworkDTO(
        name="name_example",
        description="description_example",
        deadline=1,
        subject_id="subject_id_example",
        user_id="user_id_example",
    ) # HomeworkDTO | 

    # example passing only required values which don't have defaults set
    try:
        # Save homework
        api_response = api_instance.save_homework(homework_dto)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling HomeworksApi->save_homework: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **homework_dto** | [**HomeworkDTO**](HomeworkDTO.md)|  |

### Return type

[**Homework**](Homework.md)

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

# **update_homework**
> str update_homework(id, homework_dto)

Update homework

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import openapi_client
from api.service import homeworks_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.homework_dto import HomeworkDTO
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
    api_instance = homeworks_api.HomeworksApi(api_client)
    id = "id_example" # str | Homework id
    homework_dto = HomeworkDTO(
        name="name_example",
        description="description_example",
        deadline=1,
        subject_id="subject_id_example",
        user_id="user_id_example",
    ) # HomeworkDTO | 

    # example passing only required values which don't have defaults set
    try:
        # Update homework
        api_response = api_instance.update_homework(id, homework_dto)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling HomeworksApi->update_homework: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Homework id |
 **homework_dto** | [**HomeworkDTO**](HomeworkDTO.md)|  |

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
**404** | Homework not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

